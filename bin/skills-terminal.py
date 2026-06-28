#!/usr/bin/env python3
"""Interactive terminal for a local Codex/Claude-style skills repository."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"


@dataclass(frozen=True)
class Skill:
    name: str
    description: str
    path: Path
    bucket: str


def parse_frontmatter(skill_file: Path) -> dict[str, str]:
    text = skill_file.read_text(encoding="utf-8")
    lines = text.splitlines()
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


def load_skills() -> list[Skill]:
    if not SKILLS_DIR.exists():
        return []

    skills: list[Skill] = []
    for skill_file in sorted(SKILLS_DIR.glob("**/SKILL.md")):
        skill_dir = skill_file.parent
        if not skill_dir.is_dir():
            continue
        relative = skill_dir.relative_to(SKILLS_DIR)
        bucket = relative.parts[0] if len(relative.parts) > 1 else "local"
        skill_file = skill_dir / "SKILL.md"

        metadata = parse_frontmatter(skill_file)
        name = metadata.get("name") or skill_dir.name
        description = metadata.get("description") or "Sem descricao."
        skills.append(Skill(name=name, description=description, path=skill_dir, bucket=bucket))
    return sorted(skills, key=lambda skill: (skill.bucket, skill.name))


def print_skills(skills: list[Skill]) -> None:
    if not skills:
        print("Nenhuma skill encontrada em ./skills.")
        return

    print("\nSkills disponiveis:\n")
    for index, skill in enumerate(skills, start=1):
        print(f"{index}. {skill.name} ({skill.bucket})")
        print(f"   {skill.description}")


def choose_skill(skills: list[Skill]) -> Skill | None:
    print_skills(skills)
    if not skills:
        return None

    choice = input("\nEscolha o numero da skill: ").strip()
    if not choice.isdigit():
        print("Opcao invalida.")
        return None

    index = int(choice) - 1
    if index < 0 or index >= len(skills):
        print("Opcao invalida.")
        return None

    return skills[index]


def show_skill_details(skill: Skill) -> None:
    skill_file = skill.path / "SKILL.md"
    print(f"\nNome: {skill.name}")
    print(f"Bucket: {skill.bucket}")
    print(f"Descricao: {skill.description}")
    print(f"Caminho: {skill.path.relative_to(REPO_ROOT)}")

    references_dir = skill.path / "references"
    if references_dir.exists():
        references = sorted(path.name for path in references_dir.iterdir() if path.is_file())
        if references:
            print("\nReferencias:")
            for reference in references:
                print(f"- {reference}")

    print(f"\nArquivo principal: {skill_file.relative_to(REPO_ROOT)}")


def install_skill(skill: Skill, project_path: Path, force: bool = False) -> Path:
    project_path = project_path.expanduser().resolve()
    if not project_path.exists():
        raise FileNotFoundError(f"Projeto nao encontrado: {project_path}")
    if not project_path.is_dir():
        raise NotADirectoryError(f"O caminho nao e um diretorio: {project_path}")

    target_dir = project_path / ".claude" / "skills" / skill.name
    if target_dir.exists():
        if not force:
            answer = input(f"A skill ja existe em {target_dir}. Sobrescrever? [s/n] ").strip().lower()
            if answer not in {"s", "sim", "y", "yes"}:
                print("Instalacao cancelada.")
                return target_dir
        shutil.rmtree(target_dir)

    target_dir.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(skill.path, target_dir)
    return target_dir


def find_skill(skills: list[Skill], query: str) -> Skill | None:
    matches = [
        skill
        for skill in skills
        if skill.name == query or f"{skill.bucket}/{skill.name}" == query
    ]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        mine_match = next((skill for skill in matches if skill.bucket == "mine"), None)
        return mine_match or matches[0]
    return None


def create_skill_skeleton() -> None:
    raw_name = input("Nome da nova skill (ex: audit-api): ").strip()
    name = normalize_name(raw_name)
    if not name:
        print("Nome invalido.")
        return

    raw_bucket = input("Bucket [mine/community/experiments] (padrao: mine): ").strip()
    bucket = normalize_name(raw_bucket) if raw_bucket else "mine"
    if bucket not in {"mine", "community", "experiments"}:
        print("Bucket invalido. Use mine, community ou experiments.")
        return

    target = SKILLS_DIR / bucket / name
    if target.exists():
        print(f"A skill ja existe: {target.relative_to(REPO_ROOT)}")
        return

    description = input("Descricao curta da skill: ").strip() or "Descreva quando esta skill deve ser usada."
    references_dir = target / "references"
    references_dir.mkdir(parents=True, exist_ok=True)
    (target / "SKILL.md").write_text(
        "\n".join(
            [
                "---",
                f"name: {name}",
                f"description: {description}",
                "---",
                "",
                f"# {name}",
                "",
                "Descreva aqui o fluxo principal, criterios de uso e referencias obrigatorias.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (references_dir / ".gitkeep").write_text("", encoding="utf-8")
    print(f"Skill criada em {target.relative_to(REPO_ROOT)}")


def normalize_name(value: str) -> str:
    result = []
    previous_dash = False
    for char in value.lower():
        if char.isalnum():
            result.append(char)
            previous_dash = False
        elif not previous_dash:
            result.append("-")
            previous_dash = True
    return "".join(result).strip("-")


def interactive_menu() -> None:
    while True:
        skills = load_skills()
        print(
            "\nRepositorio de Skills\n"
            "1. Listar skills\n"
            "2. Ver detalhes de uma skill\n"
            "3. Instalar skill em um projeto\n"
            "4. Criar esqueleto de nova skill\n"
            "5. Sair"
        )
        option = input("\nEscolha uma opcao: ").strip()

        if option == "1":
            print_skills(skills)
        elif option == "2":
            skill = choose_skill(skills)
            if skill:
                show_skill_details(skill)
        elif option == "3":
            skill = choose_skill(skills)
            if not skill:
                continue
            raw_path = input("\nCaminho do projeto onde instalar: ").strip()
            if not raw_path:
                print("Caminho vazio.")
                continue
            try:
                target = install_skill(skill, Path(raw_path))
                print(f"Skill instalada em {target}")
            except OSError as error:
                print(f"Erro na instalacao: {error}")
        elif option == "4":
            create_skill_skeleton()
        elif option == "5":
            return
        else:
            print("Opcao invalida.")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Terminal interativo para repositorio local de skills.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="Lista skills disponiveis.")

    install_parser = subparsers.add_parser("install", help="Instala uma skill em um projeto.")
    install_parser.add_argument("skill", help="Nome da skill.")
    install_parser.add_argument("project", help="Caminho do projeto.")
    install_parser.add_argument("--force", action="store_true", help="Sobrescreve skill existente.")

    args = parser.parse_args(argv)
    skills = load_skills()

    if args.command == "list":
        print_skills(skills)
        return 0

    if args.command == "install":
        skill = find_skill(skills, args.skill)
        if not skill:
            print(f"Skill nao encontrada: {args.skill}", file=sys.stderr)
            return 1
        try:
            target = install_skill(skill, Path(args.project), force=args.force)
        except OSError as error:
            print(f"Erro na instalacao: {error}", file=sys.stderr)
            return 1
        print(f"Skill instalada em {target}")
        return 0

    interactive_menu()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
