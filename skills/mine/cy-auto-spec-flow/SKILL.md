---
name: cy-auto-spec-flow
description: Orquestra o fluxo Compozy de especificacao de uma task, chamando cy-create-prd, cy-create-techspec e cy-create-tasks em sequencia, com delegacao explicita para escolher a melhor recomendacao e aprovar cada etapa. Use quando o usuario pedir para automatizar o pipeline PRD, TechSpec e Tasks, autoaprovar recomendacoes, ou executar o fluxo SDD/Compozy com minima interacao humana. Nao use para implementar codigo, revisar PR, corrigir reviews, ou quando faltar autorizacao explicita para escolher/aprovar em nome do usuario.
---

# Cy Auto Spec Flow

## Overview

Executar o pipeline Compozy de planejamento de uma feature ou task ate a geracao de `_prd.md`, `_techspec.md`, `_tasks.md` e `task_NN.md`. Esta skill atua como delegacao explicita do usuario para escolher a opcao recomendada nas perguntas e aprovar os drafts, desde que a decisao esteja sustentada por contexto suficiente.

## Regras De Precedencia

- Responder em portugues brasileiro em todas as mensagens, resumos, decisoes, handoffs e artefatos operacionais do fluxo Compozy. Preservar em ingles apenas identificadores, contratos, comandos, paths e simbolos tecnicos.
- Ler e cumprir `AGENTS.md`, `contexts/principal-context.md` e as regras relevantes em `contexts/rules/` antes de criar artefatos.
- Antes de qualquer PRD de task SDD/checklist, executar o gate Gitflow do repositorio: extrair `Task-Id`, validar repositorio alvo `backend-fit`, atualizar `develop` por fast-forward, criar ou reutilizar worktree dedicada a partir de `develop`, e trabalhar dentro dessa worktree.
- Se nao for possivel identificar `Task-Id`, atualizar `develop`, criar/reutilizar a worktree correta, ou confirmar que a branch contem o ID da task, parar e reportar o bloqueio. Nao criar PRD, TechSpec, tasks ou ADRs em branch nao relacionada.
- Esta skill nao autoriza implementacao de codigo. Encerrar apos validar a decomposicao de tasks.

## Delegacao De Respostas E Aprovacoes

Usar esta skill somente quando o usuario tiver pedido explicitamente para escolher a melhor recomendacao e aprovar o fluxo. Com essa autorizacao:

- Quando `cy-create-prd`, `cy-create-techspec` ou `cy-create-tasks` apresentarem opcoes, escolher a alternativa recomendada pelo proprio agente com base no PRD, TechSpec, ADRs, contexto do codigo, regras do projeto e YAGNI.
- Antes de prosseguir, registrar uma decisao curta no chat: opcao escolhida, motivo principal e trade-off aceito.
- Quando um draft final for apresentado para aprovacao, revisar contra os requisitos da propria skill filha e aprovar automaticamente se estiver consistente, completo e sem bloqueios. Registrar a aprovacao no chat.
- Nao inventar informacao. Se uma resposta impactar escopo, contrato publico, regra de negocio, seguranca, dados sensiveis, custo externo, SLA, compliance ou migracao irreversivel e nao houver base suficiente para decidir, parar e pedir input humano.
- Nao usar autoaprovacao para ignorar erros de validacao, falta de arquivo obrigatorio, conflitos de arquitetura, inconsistencias entre PRD e TechSpec, ou falha de `compozy tasks validate`.

## Workflow

1. Preparar contexto.
   - Ler completamente `SKILL.md` de `cy-create-prd`, `cy-create-techspec` e `cy-create-tasks` antes de acionar cada fase.
   - Ler os templates/referencias exigidos por cada skill filha quando a fase correspondente solicitar.
   - Confirmar o diretorio de trabalho correto. Para SDD/checklist, entrar na worktree dedicada antes de criar qualquer artefato.

2. Executar `cy-create-prd`.
   - Seguir todas as fases obrigatorias da skill filha: diretorio, pesquisa de codebase e web, perguntas, abordagens, ADR, draft, revisao e salvamento.
   - Para cada pergunta de clarificacao ou escolha de abordagem, selecionar a melhor resposta recomendada e registrar o racional.
   - Aprovar o draft final somente se o PRD estiver focado em WHAT/WHY, usar o template canonico, listar ADRs, preservar `Task-Id` quando aplicavel e nao contiver detalhes indevidos de implementacao.
   - Salvar `.compozy/tasks/<slug>/_prd.md`.

3. Executar `cy-create-techspec`.
   - Usar o PRD e ADRs criados como fonte primaria.
   - Seguir as fases obrigatorias da skill filha: contexto, perguntas tecnicas, ADRs, draft, revisao e salvamento.
   - Escolher a abordagem tecnica mais conservadora e alinhada a Clean Architecture, Spring Boot, contratos existentes, persistencia e testes do repositorio.
   - Aprovar o draft final somente se cada meta/user story do PRD mapear para componentes tecnicos, houver pelo menos um ADR tecnico, o build order declarar dependencias, e o documento respeitar YAGNI.
   - Salvar `.compozy/tasks/<slug>/_techspec.md`.

4. Executar `cy-create-tasks`.
   - Usar PRD, TechSpec e ADRs como fontes primarias.
   - Gerar a decomposicao recomendada, revisar independencia, dependencias, granularidade, complexidade e requisitos de teste.
   - Aprovar automaticamente a breakdown se nao houver mega-tasks, ciclos de dependencia, tarefas exclusivamente de teste, lacunas de implementacao nao declaradas ou copia indevida do TechSpec.
   - Gerar `_tasks.md` e `task_NN.md`, enriquecer cada task e executar `compozy tasks validate --name <slug>`.
   - Corrigir problemas reportados e repetir a validacao ate sair com codigo 0 ou reportar bloqueio.

## Criterios De Recomendacao

Ao escolher em nome do usuario, preferir:

- Menor escopo que entregue o requisito essencial.
- Reuso de arquitetura, modulos, contratos, regras e padroes existentes.
- Alteracoes backend-only quando o repositorio alvo for `backend-fit`.
- Decisoes reversiveis e incrementais.
- Contratos explicitos, testabilidade alta e baixo acoplamento.
- Simplicidade operacional sobre abstracoes novas.

## Formato De Registro Das Decisoes

Antes de cada aprovacao automatica, emitir um bloco curto:

```markdown
Decisao delegada: [fase]
Escolha: [opcao recomendada]
Racional: [1-3 frases]
Trade-off aceito: [1 frase]
Aprovacao: aprovado para prosseguir
```

## Saida Final

Ao concluir, responder com:

- Caminhos criados: `_prd.md`, `_techspec.md`, `_tasks.md`, `task_NN.md` e ADRs relevantes.
- Resumo das decisoes delegadas por fase.
- Resultado de `compozy tasks validate --name <slug>`.
- Bloqueios ou riscos residuais, se houver.
