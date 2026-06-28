# my-personal-skills

Repositorio pessoal de skills reutilizaveis para trabalhar com Compozy, agentes de IA, projetos greenfield e projetos brownfield.

As skills deste repo **nao substituem o Compozy**. Use o Compozy como fonte de verdade para PRD, TechSpec, tasks e SDD. Estas skills servem para preparar contexto, entender repositorios, validar documentacao, criar guardrails para agentes e revisar prompts/evals.

## Instalar com npx skills

Listar skills:

```bash
npx skills add Arthur-Diego/my-personal-skills --list --full-depth
```

Instalar todas no projeto atual:

```bash
npx skills add Arthur-Diego/my-personal-skills --all --full-depth
```

Instalar uma skill especifica:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-project-companion --full-depth
```

Para Claude Code:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-project-companion --agent claude-code --full-depth
```

Para Codex:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-project-companion --agent codex --full-depth
```

Observacao: se o repositorio estiver privado, autentique o GitHub na maquina antes de instalar.

## Instalar com CLI local

```bash
git clone https://github.com/Arthur-Diego/my-personal-skills.git
cd my-personal-skills
python3 bin/skills-terminal.py list
python3 bin/skills-terminal.py install <skill> /caminho/do/projeto
```

Exemplos:

```bash
python3 bin/skills-terminal.py install compozy-project-companion ~/code/meu-projeto
python3 bin/skills-terminal.py install existing-codebase-onboarding ~/code/meu-projeto
python3 bin/skills-terminal.py install agent-harness-engineer ~/code/meu-projeto
```

## Skills

- `compozy-project-companion`: orquestra o fluxo de apoio ao Compozy sem substituir SDD.
- `idea-discovery-assistant`: ajuda a escolher ideias de projeto quando ainda nao ha requisito de negocio.
- `compozy-input-brief`: transforma contexto solto em brief pronto para o Compozy.
- `existing-codebase-onboarding`: mapeia stack, arquitetura, entrypoints, testes, riscos e primeiros passos em repos existentes.
- `design-docs-auditor`: audita lacunas de Design Docs, ADRs, guidelines, contratos e operacao.
- `agent-harness-engineer`: cria/audita guardrails, gates, rubricas e execucao segura de agentes.
- `prompt-registry-and-evals`: estrutura versionamento, registry e avaliacoes de prompts.
- `refactor-arch`: audita codebases legadas e orienta refatoracao MVC.

## Greenfield

Use quando ainda nao existe projeto ou quando voce esta criando algo do zero.

### 1. Descobrir ideia

```bash
npx skills add Arthur-Diego/my-personal-skills --skill idea-discovery-assistant --full-depth
```

Resultado esperado:

- ideias candidatas;
- problema e publico;
- potencial de uso de IA;
- risco e complexidade;
- ideia recomendada.

### 2. Preparar entrada para o Compozy

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-input-brief --full-depth
```

Resultado esperado:

- contexto;
- objetivo;
- usuarios;
- restricoes;
- stack desejada;
- IA/LLM/RAG, se aplicavel;
- perguntas abertas.

Depois disso, rode o fluxo SDD no Compozy.

### 3. Preparar implementacao por agente

Depois que o Compozy gerar os artefatos:

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-project-companion --full-depth
npx skills add Arthur-Diego/my-personal-skills --skill agent-harness-engineer --full-depth
```

Resultado esperado:

- caminho de execucao recomendado;
- guardrails para agentes;
- comandos de validacao;
- criterios de qualidade;
- riscos antes da implementacao.

### 4. Se tiver IA, prompts ou RAG

```bash
npx skills add Arthur-Diego/my-personal-skills --skill prompt-registry-and-evals --full-depth
```

Resultado esperado:

- estrutura de prompts;
- versionamento;
- metadados `prompt.yaml`;
- evals/golden cases;
- criterios de qualidade.

## Brownfield

Use quando o projeto ja existe e voce precisa entrar com seguranca.

### 1. Fazer onboarding tecnico

```bash
npx skills add Arthur-Diego/my-personal-skills --skill existing-codebase-onboarding --full-depth
```

Resultado esperado:

- stack detectada;
- arquitetura atual;
- entrypoints;
- rotas/APIs;
- banco e migracoes;
- comandos de run/test/build;
- riscos;
- primeiras mudancas seguras.

### 2. Auditar documentacao tecnica

```bash
npx skills add Arthur-Diego/my-personal-skills --skill design-docs-auditor --full-depth
```

Resultado esperado:

- score de maturidade;
- lacunas de Design Docs/ADRs/guidelines/contratos/operacao;
- artefatos recomendados.

### 3. Preparar mudanca para o Compozy

```bash
npx skills add Arthur-Diego/my-personal-skills --skill compozy-input-brief --full-depth
```

Use a saida do onboarding e da auditoria como contexto para o Compozy.

### 4. Controlar execucao por agente

```bash
npx skills add Arthur-Diego/my-personal-skills --skill agent-harness-engineer --full-depth
```

Resultado esperado:

- limites de alteracao;
- gates de validacao;
- estrategia de branches/worktrees;
- evidencias necessarias;
- fallback e tratamento de falhas.

## Manutencao

Sempre que adicionar, remover ou editar skills:

```bash
python3 scripts/generate-skills-lock.py
python3 -m py_compile bin/skills-terminal.py scripts/generate-skills-lock.py
python3 bin/skills-terminal.py list
```

