# my-personal-skills

Repositorio pessoal para guardar, catalogar e instalar skills reutilizaveis em projetos.

Inspirado na organizacao de repositorios de skills como `pedronauck/skills`, este repo funciona como uma biblioteca: voce adiciona skills em `skills/`, lista pelo terminal interativo e instala a skill escolhida dentro de qualquer projeto.

## Instalacao local

Clone o repositorio:

```bash
git clone https://github.com/Arthur-Diego/my-personal-skills.git
cd my-personal-skills
```

Liste as skills disponiveis:

```bash
python3 bin/skills-terminal.py list
```

Abra o terminal interativo:

```bash
python3 bin/skills-terminal.py
```

Instale uma skill em um projeto:

```bash
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto
python3 bin/skills-terminal.py install design-docs-auditor /caminho/do/projeto
```

Isso copia a skill para:

```text
/caminho/do/projeto/.claude/skills/refactor-arch/
```

Depois, dentro do projeto:

```bash
claude "/refactor-arch"
```

## Estrutura

```text
my-personal-skills/
├── .claude/
│   └── skills/
│       └── refactor-arch/
├── .codex/
│   └── config.md
├── bin/
│   └── skills-terminal.py
├── scripts/
│   └── generate-skills-lock.py
├── skills/
│   └── mine/
│       └── refactor-arch/
│           ├── SKILL.md
│           └── references/
├── skills-lock.json
└── README.md
```

## Buckets

Use buckets para organizar a origem das skills:

- `skills/mine/`: skills autorais.
- `skills/community/`: skills externas ou adaptadas.
- `skills/experiments/`: skills em teste.

O terminal instala por nome simples:

```bash
python3 bin/skills-terminal.py install refactor-arch ~/code/meu-projeto
```

Ou por bucket:

```bash
python3 bin/skills-terminal.py install mine/refactor-arch ~/code/meu-projeto
```

## Skills disponiveis

- `refactor-arch`: audita codebases legadas e orienta refatoracao MVC.
- `design-docs-auditor`: audita repositorios e identifica lacunas de PRD, Design Docs, ADRs, guidelines, contratos e operacao.

Para usar o auditor de Design Docs diretamente:

```bash
python3 skills/design-docs-auditor/scripts/audit_design_docs.py /caminho/do/repositorio --out /caminho/do/repositorio/design-docs-audit
```

Ele gera:

```text
design-docs-audit/
├── audit.json
└── audit.md
```

## Adicionar uma nova skill

Pelo terminal interativo:

```bash
python3 bin/skills-terminal.py
```

Escolha:

```text
4. Criar esqueleto de nova skill
```

Por padrao, o esqueleto pode ser movido para um bucket:

```bash
mkdir -p skills/mine
mv skills/nova-skill skills/mine/nova-skill
```

Formato minimo:

```text
skills/mine/nova-skill/
├── SKILL.md
└── references/
```

`SKILL.md`:

```markdown
---
name: nova-skill
description: Descricao curta dizendo quando esta skill deve ser usada.
---

# Nova Skill

Instrucoes da skill.
```

Atualize o catalogo:

```bash
python3 scripts/generate-skills-lock.py
```

Versione e envie:

```bash
git add .
git commit -m "Add nova-skill"
git push
```

## Skill incluida

### refactor-arch

Audita uma codebase legada, identifica anti-patterns arquiteturais e refatora para MVC com validacao de funcionamento.

Caminho:

```text
skills/mine/refactor-arch/
```

Uso:

```bash
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto
cd /caminho/do/projeto
claude "/refactor-arch"
```

## Manutencao

Sempre que adicionar, remover ou editar uma skill, regenere:

```bash
python3 scripts/generate-skills-lock.py
```

Valide o CLI:

```bash
python3 -m py_compile bin/skills-terminal.py scripts/generate-skills-lock.py
python3 bin/skills-terminal.py list
```
