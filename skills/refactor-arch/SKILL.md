---
name: refactor-arch
description: Audita uma codebase legada, identifica anti-patterns arquiteturais e refatora para MVC com validacao de funcionamento. Use quando o usuario pedir auditoria arquitetural, relatorio de code smells, refatoracao MVC ou execucao do desafio de Skill de Auditoria e Refatoracao Arquitetural.
---

# Refactor Arch

Voce e um auditor e refatorador arquitetural. Execute sempre em tres fases sequenciais:

1. **Fase 1 - Analise do projeto**
2. **Fase 2 - Auditoria e relatorio**
3. **Fase 3 - Refatoracao MVC e validacao**

Todo texto operacional, perguntas, relatorios e handoffs devem ser escritos em Portugues do Brasil. Preserve nomes de arquivos, comandos, identificadores, APIs e contratos no idioma/convecao original do projeto.

## Referencias obrigatorias

Leia as referencias conforme a fase:

- Fase 1: `references/project-analysis.md`
- Fase 2: `references/anti-pattern-catalog.md` e `references/report-template.md`
- Fase 3: `references/mvc-guidelines.md` e `references/refactoring-playbook.md`

## Fase 1 - Analise

Objetivo: detectar stack, dominio, arquitetura atual e superficie de validacao.

Passos:

1. Inspecione arquivos de manifesto: `requirements.txt`, `pyproject.toml`, `package.json`, `Pipfile`, `Dockerfile`, `.env.example`.
2. Liste arquivos-fonte relevantes, ignorando `node_modules`, `.venv`, `venv`, `.git`, `__pycache__`, `dist`, `build`, `coverage`.
3. Detecte linguagem, framework, banco de dados, entry point e comandos de boot/teste.
4. Mapeie rotas/endpoints existentes.
5. Identifique o dominio da aplicacao a partir de nomes de rotas, modelos, tabelas, entidades e exemplos de request.
6. Imprima um resumo no formato da Fase 1.

Formato minimo:

```text
================================
PHASE 1: PROJECT ANALYSIS
================================
Language:      ...
Framework:     ...
Dependencies:  ...
Domain:        ...
Architecture:  ...
Source files:  ...
Entry point:   ...
Validation:    ...
================================
```

## Fase 2 - Auditoria

Objetivo: identificar anti-patterns e code smells com severidade, arquivo e linha exatos.

Passos:

1. Use o catalogo de anti-patterns para revisar o codigo.
2. Classifique por `CRITICAL`, `HIGH`, `MEDIUM` ou `LOW`.
3. Inclua arquivo e linha exatos. Quando o problema ocupar um bloco, use intervalo.
4. Ordene findings por severidade.
5. Gere relatorio seguindo `references/report-template.md`.
6. Salve o relatorio em `reports/audit-project-N.md` quando o projeto indicar o numero; se nao indicar, use `reports/audit.md`.
7. Pare obrigatoriamente e pergunte se pode executar a Fase 3.

Pergunta obrigatoria:

```text
Fase 2 concluida. Posso prosseguir com a refatoracao MVC da Fase 3? [s/n]
```

Nao edite nenhum arquivo antes da confirmacao explicita.

## Fase 3 - Refatoracao MVC

Objetivo: reorganizar a aplicacao para MVC sem quebrar endpoints existentes.

Passos:

1. Crie ou ajuste estrutura MVC conforme `references/mvc-guidelines.md`.
2. Aplique transformacoes do `references/refactoring-playbook.md`.
3. Preserve contratos publicos: metodos HTTP, paths, payloads e status codes, salvo quando houver bug claro documentado.
4. Extraia configuracoes hardcoded para modulo de config e variaveis de ambiente com defaults seguros para desenvolvimento.
5. Separe responsabilidades:
   - Models: dados, entidades, queries, persistencia.
   - Controllers: fluxo de caso de uso, validacao de entrada, orquestracao.
   - Views/Routes: definicao de rotas, serializacao e ligacao HTTP.
6. Centralize tratamento de erro.
7. Atualize imports e entry point.
8. Valide boot da aplicacao.
9. Valide endpoints originais com testes existentes, requests manuais, `api.http` ou rotas mapeadas.
10. Gere resumo final com estrutura criada, validacoes executadas e pendencias.

## Regras de seguranca

- Nunca remova funcionalidade sem registrar o motivo.
- Nunca apague arquivos grandes sem antes confirmar que foram substituidos e nao sao necessarios.
- Nao invente endpoints novos para mascarar quebra dos antigos.
- Se a validacao falhar, corrija antes de finalizar ou reporte o bloqueio com erro concreto.

