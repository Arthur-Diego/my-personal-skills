#!/usr/bin/env python3
import argparse
import json
import os
import re
from pathlib import Path

IGNORE = {".git", "node_modules", ".venv", "venv", "dist", "build", ".next", "coverage", "__pycache__", "target", "vendor", "data"}
MANIFESTS = ["package.json", "requirements.txt", "pyproject.toml", "go.mod", "Cargo.toml", "pom.xml", "build.gradle", "Makefile", "Dockerfile", "docker-compose.yml"]


def iter_files(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for name in files:
            yield Path(current) / name


def read(path: Path, limit=80000):
    try:
        return path.read_bytes()[:limit].decode("utf-8", errors="ignore")
    except OSError:
        return ""


def rel(path: Path, root: Path):
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def detect(root: Path):
    files = list(iter_files(root))
    names = {rel(p, root) for p in files}
    lower = "\n".join(n.lower() for n in names)
    source_files = [p for p in files if p.suffix.lower() in {".py", ".js", ".ts", ".tsx", ".go", ".java", ".rb"}]
    sample = "\n".join(read(p, 30000).lower() for p in source_files[:120])
    manifests = [m for m in MANIFESTS if (root / m).exists()]
    stack = []
    if "package.json" in names:
        stack.append("Node.js/JavaScript/TypeScript")
    if "requirements.txt" in names or "pyproject.toml" in names:
        stack.append("Python")
    if "go.mod" in names:
        stack.append("Go")
    if "Cargo.toml" in names:
        stack.append("Rust")
    frameworks = []
    patterns = {
        "FastAPI": "fastapi",
        "Flask": "flask",
        "Django": "django",
        "Express": "express",
        "Next.js": "next",
        "React": "react",
        "NestJS": "nestjs",
        "Spring": "spring",
    }
    for label, pattern in patterns.items():
        if pattern in sample + lower:
            frameworks.append(label)
    routes = []
    route_re = re.compile(r"(@app\.(get|post|put|delete|patch)\(|router\.(get|post|put|delete|patch)\(|app\.(get|post|put|delete|patch)\()", re.I)
    for p in files:
        if p.suffix.lower() in {".py", ".js", ".ts", ".tsx"} and route_re.search(read(p, 20000)):
            routes.append(rel(p, root))
    tests = [rel(p, root) for p in files if re.search(r"(test|spec)", p.name, re.I)]
    docs = [rel(p, root) for p in files if p.suffix.lower() in {".md", ".mdx", ".rst"}]
    return {
        "root": str(root),
        "counts": {"files": len(files), "docs": len(docs), "tests": len(tests), "route_files": len(routes)},
        "manifests": manifests,
        "stack": stack,
        "frameworks": frameworks,
        "route_files": routes[:40],
        "tests": tests[:40],
        "docs": docs[:40],
        "signals": {
            "has_env_example": (root / ".env.example").exists(),
            "has_docker": "Dockerfile" in names or "docker-compose.yml" in names,
            "has_ci": ".github/workflows" in lower,
            "has_database": bool(re.search(r"(migration|schema|prisma|sqlalchemy|typeorm|sequelize|create table)", sample + lower)),
            "has_auth": bool(re.search(r"(auth|jwt|oauth|session|password|role|permission)", sample + lower)),
        },
    }


def render(result):
    lines = [
        "# Onboarding técnico",
        "",
        "## Resumo",
        f"- Arquivos analisados: {result['counts']['files']}",
        f"- Stack: {', '.join(result['stack']) or 'não detectada'}",
        f"- Frameworks: {', '.join(result['frameworks']) or 'não detectados'}",
        "",
        "## Manifests",
        *[f"- `{m}`" for m in result["manifests"]],
        "",
        "## Rotas / APIs prováveis",
        *[f"- `{p}`" for p in result["route_files"]],
        "",
        "## Testes",
        *[f"- `{p}`" for p in result["tests"][:20]],
        "",
        "## Documentação",
        *[f"- `{p}`" for p in result["docs"][:20]],
        "",
        "## Sinais",
        *[f"- {k}: {v}" for k, v in result["signals"].items()],
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--out")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    result = detect(root)
    out = Path(args.out).resolve() if args.out else root / "onboarding-report"
    out.mkdir(parents=True, exist_ok=True)
    (out / "onboarding.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "onboarding.md").write_text(render(result), encoding="utf-8")
    print(json.dumps({"out": str(out), **result["counts"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
