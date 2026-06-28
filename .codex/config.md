# Personal Skills Repository

Este repositorio armazena skills reutilizaveis.

Convencoes:

- Skills autorais ficam em `skills/mine/<skill-name>/`.
- Skills externas ou adaptadas podem ficar em `skills/community/<skill-name>/`.
- Cada skill precisa ter `SKILL.md` com frontmatter `name` e `description`.
- O catalogo `skills-lock.json` deve ser regenerado apos adicionar ou editar skills.

Comandos:

```bash
python3 bin/skills-terminal.py
python3 bin/skills-terminal.py list
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto
python3 scripts/generate-skills-lock.py
```
