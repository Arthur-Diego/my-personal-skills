#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


CHECKS = {
    "agent_instructions": ["AGENTS.md", "CLAUDE.md", ".cursor/rules", ".codex"],
    "env_example": [".env.example", ".env.sample"],
    "ci": [".github/workflows", ".gitlab-ci.yml"],
    "tests": ["pytest.ini", "vitest.config.ts", "jest.config.js", "playwright.config.ts", "tests", "test", "__tests__"],
    "docs": ["docs", "README.md"],
    "scripts": ["Makefile", "package.json", "pyproject.toml"],
}


def exists(root: Path, candidates: list[str]):
    found = []
    for item in candidates:
        path = root / item
        if path.exists():
            found.append(item)
    return found


def audit(root: Path):
    coverage = {key: exists(root, values) for key, values in CHECKS.items()}
    score = int(sum(1 for values in coverage.values() if values) / len(coverage) * 100)
    missing = [key for key, values in coverage.items() if not values]
    return {"root": str(root), "score": score, "coverage": coverage, "missing": missing}


def render(result):
    lines = ["# Agent Harness Audit", "", f"- Score: {result['score']}/100", "", "## Coverage"]
    for key, values in result["coverage"].items():
        lines.append(f"- {key}: {', '.join(values) if values else 'missing'}")
    lines += ["", "## Recommended Actions"]
    for item in result["missing"]:
        lines.append(f"- Add or document `{item}` guardrails.")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--out")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    result = audit(root)
    out = Path(args.out).resolve() if args.out else root / "harness-audit"
    out.mkdir(parents=True, exist_ok=True)
    (out / "harness.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "harness.md").write_text(render(result), encoding="utf-8")
    print(json.dumps({"score": result["score"], "missing": result["missing"], "out": str(out)}, ensure_ascii=False))


if __name__ == "__main__":
    main()

