# my-personal-skills

Skills para trabalhar com **Compozy + agentes de IA** em projetos greenfield e brownfield.

O Compozy continua sendo a fonte de verdade para **PRD, TechSpec, tasks e SDD**.  
Estas skills preparam contexto, validam riscos e organizam a execucao por agentes.

Legenda:

- `[AUTO]`: feito por uma skill/agente.
- `[MANUAL]`: feito por voce fora da skill.

As skills **nao executam o Compozy automaticamente**. Elas preparam a entrada e validam a saida.

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

Rode ela novamente quando:

- iniciar uma nova feature ou wave de tasks;
- o Compozy atualizar artefatos;
- for entregar trabalho para um agente;
- uma wave terminar;
- testes falharem ou nao puderem rodar;
- mudar arquitetura, banco, API, auth, deploy, prompts, RAG ou evals;
- o proximo passo ficar ambiguo.

Nao precisa rodar de novo para task pequena, isolada e com validacao obvia.

## Fluxo Greenfield

```text
1. [AUTO] idea-discovery-assistant
   Descobre ideia, problema, publico, risco e potencial de IA.

        |
        v

2. [AUTO] compozy-input-brief
   Transforma a ideia em um brief limpo para voce usar no Compozy.

        |
        v

3. [MANUAL] Rodar Compozy
   Voce executa seu fluxo Compozy para gerar PRD, TechSpec, tasks e SDD.

        |
        v

4. [AUTO] compozy-project-companion
   Le os resultados/contexto e decide proximas skills.

        |
        v

5. [AUTO] agent-harness-engineer
   Cria guardrails, gates, comandos e criterios para agentes.

        |
        v

6. [AUTO] prompt-registry-and-evals
   Use se houver IA, prompts, RAG ou LLM em producao.
```

## Fluxo Brownfield

```text
1. [AUTO] existing-codebase-onboarding
   Mapeia stack, arquitetura, entrypoints, APIs, testes e riscos.

        |
        v

2. [AUTO] design-docs-auditor
   Audita lacunas de Design Docs, ADRs, contratos e operacao.

        |
        v

3. [AUTO] compozy-input-brief
   Prepara o contexto do projeto existente para voce usar no Compozy.

        |
        v

4. [MANUAL] Rodar Compozy
   Voce executa o Compozy para gerar ou atualizar os artefatos SDD.

        |
        v

5. [AUTO] agent-harness-engineer
   Define limites, validacoes, evidencias e estrategia de execucao.

        |
        v

6. [AUTO] refactor-arch
   Use quando o foco for auditoria/refatoracao arquitetural.
```

## Skills

| Skill | Faz |
| --- | --- |
| `compozy-project-companion` | Orquestra o fluxo; nao chama o Compozy. |
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
