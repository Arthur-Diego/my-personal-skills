#!/usr/bin/env python3
import argparse
import json
import os
import re
from dataclasses import dataclass, asdict
from pathlib import Path


DOC_EXTENSIONS = {".md", ".mdx", ".txt", ".rst", ".adoc"}
CODE_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".java", ".kt", ".rs", ".rb",
    ".php", ".cs", ".swift", ".c", ".cc", ".cpp", ".h", ".hpp", ".sql", ".yml", ".yaml",
    ".json", ".toml", ".tf", ".dockerfile",
}
IGNORE_DIRS = {
    ".git", "node_modules", ".venv", "venv", "dist", "build", ".next", ".nuxt",
    "coverage", "__pycache__", ".terraform", "vendor", "target", ".idea", ".vscode",
    "data", "tmp", "temp", "logs", "design-docs-audit",
}
DOC_NAME_EXCLUDE = {
    "requirements.txt", "package-lock.json", "yarn.lock", "pnpm-lock.yaml",
    "poetry.lock", "pipfile.lock", "go.sum", "cargo.lock",
}


@dataclass
class Finding:
    severity: str
    category: str
    title: str
    evidence: str
    recommendation: str


def read_text(path: Path, limit: int = 240_000) -> str:
    try:
        data = path.read_bytes()[:limit]
        return data.decode("utf-8", errors="ignore")
    except OSError:
        return ""


def iter_files(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".cache")]
        base = Path(current)
        for name in files:
            path = base / name
            if name.lower() in DOC_NAME_EXCLUDE:
                continue
            if path.is_file():
                yield path


def rel(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def classify_docs(root: Path):
    docs = []
    code = []
    for path in iter_files(root):
        suffix = path.suffix.lower()
        name = path.name.lower()
        if suffix in DOC_EXTENSIONS or name in {"readme", "dockerfile"}:
            docs.append(path)
        elif suffix in CODE_EXTENSIONS or name in {"dockerfile", "makefile"}:
            code.append(path)
    return docs, code


def contains_any(text: str, patterns: list[str]) -> bool:
    lower = text.lower()
    return any(pattern in lower for pattern in patterns)


def matching_docs(root: Path, docs: list[Path], name_patterns: list[str], content_patterns: list[str]):
    matches = []
    for path in docs:
        r = rel(path, root).lower()
        text = read_text(path).lower()
        if any(pattern in r for pattern in name_patterns) or any(pattern in text for pattern in content_patterns):
            matches.append(path)
    return matches


def repo_signals(root: Path, code: list[Path]) -> dict:
    names = {rel(p, root).lower() for p in code}
    all_paths = "\n".join(names)
    text_sample = "\n".join(read_text(p, 40_000).lower() for p in code[:200])
    return {
        "has_api": bool(re.search(r"(route|router|controller|endpoint|fastapi|express|nestjs|spring|gin|fiber)", text_sample)),
        "has_db": bool(re.search(r"(migration|schema|prisma|typeorm|sequelize|sqlalchemy|django.db|create table|alter table)", text_sample + all_paths)),
        "has_auth": bool(re.search(r"(auth|jwt|oauth|session|password|permission|role)", text_sample + all_paths)),
        "has_deploy": any(x in all_paths for x in ["dockerfile", "docker-compose", ".github/workflows", "terraform", "helm", "k8s", "kubernetes"]),
        "has_tests": bool(re.search(r"(test|spec|pytest|jest|vitest|junit|rspec)", all_paths)),
        "has_env": any(Path(root, p).exists() for p in [".env.example", ".env.sample"]),
    }


def dedicated(paths: list[Path], root: Path) -> list[Path]:
    result = []
    for path in paths:
        r = rel(path, root).lower()
        if Path(r).name.startswith("readme"):
            continue
        result.append(path)
    return result


def audit(root: Path) -> dict:
    docs, code = classify_docs(root)
    signals = repo_signals(root, code)

    prd_docs = matching_docs(root, docs, ["prd", "product", "requirements", "spec"], ["problem statement", "non-goals", "acceptance criteria", "functional requirements"])
    design_docs = matching_docs(root, docs, ["design", "architecture", "technical-spec", "techspec", "system"], ["architecture", "tradeoff", "alternatives considered", "data flow", "sequence diagram"])
    adr_docs = matching_docs(root, docs, ["adr", "decision", "decisions"], ["status:", "context", "decision", "consequences", "alternatives"])
    guideline_docs = matching_docs(root, docs, ["agents.md", "contributing", "guideline", "testing"], ["definition of done", "coding standard", "review", "test strategy"])
    ops_docs = matching_docs(root, docs, ["deploy", "operations", "runbook", "observability", "security"], ["rollback", "environment variables", "health check", "metrics", "logs", "secrets"])
    contract_docs = matching_docs(root, docs, ["api", "contract", "openapi", "swagger", "schema"], ["openapi", "endpoint", "request", "response", "event", "schema"])
    prd_effective = dedicated(prd_docs, root)
    design_effective = dedicated(design_docs, root)
    adr_effective = dedicated(adr_docs, root)
    ops_effective = dedicated(ops_docs, root)
    contract_effective = dedicated(contract_docs, root)

    findings: list[Finding] = []

    if not prd_effective:
        evidence = "Only README-level product notes were found." if prd_docs else "No PRD/requirements/spec document matched repository docs."
        findings.append(Finding("High", "Product intent", "Dedicated PRD or requirements document not found", evidence, "Create docs/prd.md with problem, goals, non-goals, users, requirements, and acceptance criteria."))
    if not design_effective:
        severity = "High" if len(code) > 20 or signals["has_api"] or signals["has_db"] else "Medium"
        evidence = "Only README-level architecture notes were found." if design_docs else "No design, architecture, or technical spec document matched repository docs."
        findings.append(Finding(severity, "Technical design", "Dedicated design/architecture document not found", evidence, "Create docs/design/system-overview.md or docs/architecture.md explaining components, data flow, contracts, tradeoffs, and failure modes."))
    if not adr_effective:
        severity = "High" if signals["has_db"] or signals["has_auth"] or signals["has_deploy"] else "Medium"
        evidence = "Only README-level decision notes were found." if adr_docs else "No ADR or decision-record document matched repository docs."
        findings.append(Finding(severity, "Decision records", "ADR/decision log not found", evidence, "Create docs/adr/0001-record-architecture-baseline.md and use ADRs for database, auth, framework, and deployment decisions."))
    if not guideline_docs:
        findings.append(Finding("Medium", "Engineering guidelines", "Engineering guidelines are missing or weak", "No AGENTS.md/CONTRIBUTING/testing/guidelines document matched repository docs.", "Add AGENTS.md or docs/engineering-guidelines.md with coding, testing, review, and AI-agent rules."))
    if signals["has_deploy"] and not ops_effective:
        evidence = "Only README-level operational notes were found." if ops_docs else "Deployment/config files were detected, but no runbook/deployment/operations/security documentation matched."
        findings.append(Finding("High", "Operations", "Deployment signals exist without dedicated operational docs", evidence, "Create docs/operations.md with env vars, deployment steps, health checks, rollback, logs, and troubleshooting."))
    elif not ops_effective:
        evidence = "Only README-level operational notes were found." if ops_docs else "No operations, deployment, runbook, observability, or security docs matched."
        findings.append(Finding("Medium", "Operations", "Dedicated operational documentation not found", evidence, "Create docs/operations.md scaled to the project risk."))
    if signals["has_api"] and not contract_effective:
        evidence = "Only README-level API notes were found." if contract_docs else "API-like code was detected, but no API/contract/OpenAPI documentation matched."
        findings.append(Finding("High", "Contracts", "API or integration contracts not documented", evidence, "Document endpoints/events in docs/contracts/api.md or add an OpenAPI spec."))
    if signals["has_env"] and not ops_effective:
        findings.append(Finding("Medium", "Environment", ".env example exists without operational explanation", ".env.example/.env.sample detected, but no operational documentation matched.", "Document every env var, secret source, default, and production expectation."))
    if signals["has_tests"] and not guideline_docs:
        findings.append(Finding("Medium", "Testing", "Tests exist without test strategy documentation", "Test files were detected, but no testing strategy/guideline document matched.", "Add docs/testing.md describing required test layers and acceptance gates."))

    coverage = {
        "prd": [rel(p, root) for p in prd_effective],
        "design": [rel(p, root) for p in design_effective],
        "adr": [rel(p, root) for p in adr_effective],
        "guidelines": [rel(p, root) for p in guideline_docs],
        "operations": [rel(p, root) for p in ops_effective],
        "contracts": [rel(p, root) for p in contract_effective],
    }
    raw_matches = {
        "prd": [rel(p, root) for p in prd_docs],
        "design": [rel(p, root) for p in design_docs],
        "adr": [rel(p, root) for p in adr_docs],
        "operations": [rel(p, root) for p in ops_docs],
        "contracts": [rel(p, root) for p in contract_docs],
    }
    weights = {"prd": 15, "design": 25, "adr": 15, "guidelines": 15, "operations": 15, "contracts": 15}
    score = sum(weights[key] for key, paths in coverage.items() if paths)
    if signals["has_api"] and not coverage["contracts"]:
        score -= 10
    if signals["has_deploy"] and not coverage["operations"]:
        score -= 10
    score = max(0, min(100, score))

    return {
        "root": str(root),
        "score": score,
        "coverage_label": "strong" if score >= 80 else "partial" if score >= 45 else "weak",
        "signals": signals,
        "counts": {"docs": len(docs), "code": len(code), "findings": len(findings)},
        "coverage": coverage,
        "raw_matches": raw_matches,
        "findings": [asdict(item) for item in findings],
        "recommended_artifacts": recommended_artifacts(findings),
    }


def recommended_artifacts(findings: list[Finding]) -> list[dict]:
    mapping = {
        "Product intent": ("docs/prd.md", "Define product intent, scope, requirements, and acceptance criteria."),
        "Technical design": ("docs/design/system-overview.md", "Document architecture, components, data flow, contracts, tradeoffs, and failure modes."),
        "Decision records": ("docs/adr/0001-architecture-baseline.md", "Record important technical decisions with context and consequences."),
        "Engineering guidelines": ("AGENTS.md", "Define coding, testing, review, and AI-agent operating rules."),
        "Operations": ("docs/operations.md", "Document env vars, deployment, health checks, observability, rollback, and troubleshooting."),
        "Contracts": ("docs/contracts/api.md", "Document API/event/request/response contracts."),
        "Environment": ("docs/operations.md", "Explain env vars, defaults, secret handling, and deployment values."),
        "Testing": ("docs/testing.md", "Describe test strategy and required validation gates."),
    }
    seen = set()
    artifacts = []
    for finding in findings:
        path, reason = mapping.get(finding.category, ("docs/design/README.md", finding.recommendation))
        if path not in seen:
            seen.add(path)
            artifacts.append({"path": path, "reason": reason})
    return artifacts


def render_markdown(result: dict) -> str:
    lines = [
        "# Design Docs Audit",
        "",
        f"- Score: {result['score']}/100",
        f"- Coverage: {result['coverage_label']}",
        f"- Docs scanned: {result['counts']['docs']}",
        f"- Code/config files scanned: {result['counts']['code']}",
        "",
        "## Coverage",
        "",
    ]
    for key, paths in result["coverage"].items():
        label = "present" if paths else "missing"
        lines.append(f"- {key}: {label}" + (f" ({', '.join(paths[:5])})" if paths else ""))
    lines.extend(["", "## Findings", ""])
    if not result["findings"]:
        lines.append("No major Design Docs gaps detected by the automated pass.")
    for idx, finding in enumerate(result["findings"], 1):
        lines.extend([
            f"### {idx}. [{finding['severity']}] {finding['title']}",
            "",
            f"- Category: {finding['category']}",
            f"- Evidence: {finding['evidence']}",
            f"- Recommendation: {finding['recommendation']}",
            "",
        ])
    lines.extend(["## Recommended Artifacts", ""])
    for artifact in result["recommended_artifacts"]:
        lines.append(f"- `{artifact['path']}`: {artifact['reason']}")
    lines.extend(["", "## Repository Signals", ""])
    for key, value in result["signals"].items():
        lines.append(f"- {key}: {value}")
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit repository Design Docs readiness.")
    parser.add_argument("repo", nargs="?", default=".", help="Repository path to audit.")
    parser.add_argument("--out", help="Output directory for JSON and Markdown reports.")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Repository path not found: {root}")

    result = audit(root)
    output = Path(args.out).resolve() if args.out else root / "design-docs-audit"
    output.mkdir(parents=True, exist_ok=True)
    (output / "audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    (output / "audit.md").write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps({"score": result["score"], "coverage": result["coverage_label"], "findings": len(result["findings"]), "out": str(output)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
