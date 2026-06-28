# my-personal-skills

Skills para trabalhar com **Compozy + agentes de IA** em projetos greenfield e brownfield.

O Compozy continua sendo a fonte de verdade para **PRD, TechSpec, tasks e SDD**.  
Estas skills preparam contexto, validam riscos e organizam a execucao por agentes.

## Instalar

```bash
npx skills add Arthur-Diego/my-personal-skills --list --full-depth
npx skills add Arthur-Diego/my-personal-skills --skill compozy-project-companion --full-depth
```

Para instalar tudo:

```bash
npx skills add Arthur-Diego/my-personal-skills --all --full-depth
```

CLI local:

```bash
git clone https://github.com/Arthur-Diego/my-personal-skills.git
cd my-personal-skills
python3 bin/skills-terminal.py install compozy-project-companion /caminho/do/projeto
```

## Skill principal

`compozy-project-companion` e a skill orquestradora.

Ela decide o caminho:

```text
                compozy-project-companion
                         |
        +----------------+----------------+
        |                                 |
   Greenfield                         Brownfield
 projeto novo                     projeto existente
```

## Fluxo Greenfield

```text
1. idea-discovery-assistant
   Descobre ideia, problema, publico, risco e potencial de IA.

        |
        v

2. compozy-input-brief
   Transforma a ideia em um brief limpo para o Compozy.

        |
        v

3. Compozy
   Gera PRD, TechSpec, tasks e fluxo SDD.

        |
        v

4. compozy-project-companion
   Decide proximas skills e checa se a execucao esta pronta.

        |
        v

5. agent-harness-engineer
   Cria guardrails, gates, comandos e criterios para agentes.

        |
        v

6. prompt-registry-and-evals
   Use se houver IA, prompts, RAG ou LLM em producao.
```

## Fluxo Brownfield

```text
1. existing-codebase-onboarding
   Mapeia stack, arquitetura, entrypoints, APIs, testes e riscos.

        |
        v

2. design-docs-auditor
   Audita lacunas de Design Docs, ADRs, contratos e operacao.

        |
        v

3. compozy-input-brief
   Prepara o contexto do projeto existente para o Compozy.

        |
        v

4. Compozy
   Gera ou atualiza os artefatos SDD.

        |
        v

5. agent-harness-engineer
   Define limites, validacoes, evidencias e estrategia de execucao.

        |
        v

6. refactor-arch
   Use quando o foco for auditoria/refatoracao arquitetural.
```

## Skills

| Skill | Faz |
| --- | --- |
| `compozy-project-companion` | Orquestra o fluxo e escolhe quais skills usar. |
| `idea-discovery-assistant` | Ajuda a encontrar uma ideia de projeto viavel. |
| `compozy-input-brief` | Cria um brief de entrada para o Compozy. |
| `existing-codebase-onboarding` | Explica um repo existente antes de mexer nele. |
| `design-docs-auditor` | Encontra lacunas de Design Docs, ADRs e operacao. |
| `agent-harness-engineer` | Define guardrails e validacoes para agentes. |
| `prompt-registry-and-evals` | Organiza prompts, versoes e avaliacoes. |
| `refactor-arch` | Audita e orienta refatoracao arquitetural. |

## Manutencao

```bash
python3 scripts/generate-skills-lock.py
python3 -m py_compile bin/skills-terminal.py scripts/generate-skills-lock.py
python3 bin/skills-terminal.py list
```

