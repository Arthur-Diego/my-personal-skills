# my-personal-skills

Repositorio pessoal para guardar, catalogar e instalar skills reutilizaveis em projetos.

Inspirado na organizacao de repositorios de skills como `pedronauck/skills`, este repo funciona como uma biblioteca: voce adiciona skills em `skills/`, lista pelo CLI `npx skills` e instala a skill escolhida dentro de qualquer projeto.

## Instalacao via npx

Listar as skills disponiveis no repositorio:

```bash
npx skills add Arthur-Diego/my-personal-skills --list --full-depth
```

Instalar todas as skills no projeto atual:

```bash
npx skills add Arthur-Diego/my-personal-skills --all --full-depth
```

Instalar uma skill especifica no projeto atual:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill refactor-arch --full-depth
```

Instalar uma skill especifica para Claude Code:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill refactor-arch --agent claude-code --full-depth
```

Instalar uma skill especifica para Codex:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill refactor-arch --agent codex --full-depth
```

Instalar globalmente para o usuario:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill refactor-arch --global --full-depth
```

Buscar skills de forma interativa:

```bash
npx skills find --owner Arthur-Diego
```

Depois, dentro do projeto, use a skill pelo nome:

```bash
claude "/refactor-arch"
```

Quando o agente detectado for Codex, o instalador usa `.agents/skills/...`. Quando voce passa `--agent claude-code`, ele instala em `.claude/skills/...`.

Observacao: este repositorio esta privado. O `npx skills` funcionou localmente porque o GitHub ja esta autenticado nesta maquina. Em outra maquina, autentique primeiro com `gh auth login` ou torne o repositorio publico.

## Instalacao local alternativa

Clone o repositorio:

```bash
git clone https://github.com/Arthur-Diego/my-personal-skills.git
cd my-personal-skills
```

Liste as skills disponiveis:

```bash
python3 bin/skills-terminal.py list
```

Abra o terminal interativo local:

```bash
python3 bin/skills-terminal.py
```

Instale uma skill em um projeto especifico:

```bash
python3 bin/skills-terminal.py install refactor-arch /caminho/do/projeto
python3 bin/skills-terminal.py install design-docs-auditor /caminho/do/projeto
python3 bin/skills-terminal.py install compozy-project-companion /caminho/do/projeto
```

O instalador local copia a skill para:

```text
/caminho/do/projeto/.claude/skills/refactor-arch/
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
- `compozy-project-companion`: orquestra o fluxo de apoio ao Compozy sem substituir o SDD.
- `idea-discovery-assistant`: ajuda a escolher ideias de projeto quando ainda nao ha requisitos de negocio.
- `compozy-input-brief`: transforma contexto solto em um brief pronto para usar no Compozy.
- `existing-codebase-onboarding`: mapeia stack, arquitetura, entrypoints, testes, riscos e primeiros passos em repos existentes.
- `agent-harness-engineer`: cria e audita guardrails, gates, rubricas e execucao segura de agentes.
- `prompt-registry-and-evals`: estrutura versionamento, registry e avaliacoes de prompts.

## Fluxo recomendado com Compozy

As skills deste repositorio nao substituem o Compozy. Use o Compozy como fonte de verdade para PRD, TechSpec, tasks e SDD. As skills ajudam antes e depois desse fluxo.

Projeto novo sem ideia:

```text
idea-discovery-assistant
-> compozy-input-brief
-> Compozy
-> compozy-project-companion
-> agent-harness-engineer
-> implementacao por agente
```

Projeto existente:

```text
existing-codebase-onboarding
-> design-docs-auditor
-> compozy-input-brief
-> Compozy
-> agent-harness-engineer
-> implementacao por agente
```

Feature com IA, prompts ou RAG:

```text
compozy-input-brief
-> Compozy
-> prompt-registry-and-evals
-> agent-harness-engineer
-> implementacao por agente
```

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

### Kit Compozy + IA

Skills autorais adicionadas para projetos com Compozy, agentes e Applied AI Engineering:

```text
skills/mine/compozy-project-companion/
skills/mine/idea-discovery-assistant/
skills/mine/compozy-input-brief/
skills/mine/existing-codebase-onboarding/
skills/mine/agent-harness-engineer/
skills/mine/prompt-registry-and-evals/
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
