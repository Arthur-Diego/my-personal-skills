#!/usr/bin/env python3
"""Generate skills-lock.json from skills/**/SKILL.md files."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
LOCK_FILE = ROOT / "skills-lock.json"


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    skills = []
    for skill_file in sorted(SKILLS_DIR.glob("**/SKILL.md")):
        skill_dir = skill_file.parent
        relative = skill_dir.relative_to(ROOT)
        metadata = parse_frontmatter(skill_file)
        parts = skill_dir.relative_to(SKILLS_DIR).parts
        bucket = parts[0] if len(parts) > 1 else "local"
        name = metadata.get("name") or skill_dir.name
        skills.append(
            {
                "name": name,
                "bucket": bucket,
                "path": str(relative),
                "description": metadata.get("description", ""),
            }
        )

    payload = {
        "version": 1,
        "repository": "my-personal-skills",
        "skills": skills,
    }
    LOCK_FILE.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Generated {LOCK_FILE.relative_to(ROOT)} with {len(skills)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
