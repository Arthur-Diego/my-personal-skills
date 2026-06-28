#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

IGNORE = {".git", "node_modules", ".venv", "venv", "dist", "build", "data"}
PROMPT_HINTS = ("prompt", "prompts", "langsmith", "eval", "golden")


def iter_files(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for name in files:
            yield Path(current) / name


def rel(path: Path, root: Path):
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def audit(root: Path):
    files = list(iter_files(root))
    prompt_files = [rel(p, root) for p in files if any(h in rel(p, root).lower() for h in PROMPT_HINTS)]
    yaml_files = [p for p in prompt_files if p.endswith((".yaml", ".yml"))]
    md_files = [p for p in prompt_files if p.endswith((".md", ".txt"))]
    eval_files = [p for p in prompt_files if "eval" in p.lower() or "golden" in p.lower()]
    score = 0
    if prompt_files:
        score += 30
    if yaml_files:
        score += 25
    if eval_files:
        score += 30
    if any("prompts/" in p or p.startswith("prompts") for p in prompt_files):
        score += 15
    return {
        "root": str(root),
        "score": min(score, 100),
        "prompt_files": prompt_files[:100],
        "yaml_files": yaml_files[:50],
        "md_files": md_files[:50],
        "eval_files": eval_files[:50],
    }


def render(result):
    lines = ["# Prompt Registry Audit", "", f"- Score: {result['score']}/100", "", "## Prompt files"]
    lines += [f"- `{p}`" for p in result["prompt_files"]] or ["- none"]
    lines += ["", "## Gaps"]
    if not result["prompt_files"]:
        lines.append("- No prompt registry or prompt files detected.")
    if not result["yaml_files"]:
        lines.append("- No prompt metadata YAML detected.")
    if not result["eval_files"]:
        lines.append("- No prompt eval/golden dataset files detected.")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--out")
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    result = audit(root)
    out = Path(args.out).resolve() if args.out else root / "prompt-registry-audit"
    out.mkdir(parents=True, exist_ok=True)
    (out / "prompt-registry.json").write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    (out / "prompt-registry.md").write_text(render(result), encoding="utf-8")
    print(json.dumps({"score": result["score"], "out": str(out), "prompt_files": len(result["prompt_files"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()

