---
name: compozy-project-companion
description: Orchestrate a Compozy-centered project workflow without replacing Compozy SDD. Use when starting a new project, entering an existing codebase, preparing a brief for Compozy, reviewing Compozy-generated artifacts, or deciding which companion skills to run before or after Compozy execution.
---

# Compozy Project Companion

Use this skill as the router for projects that use Compozy as the SDD source of truth. Write all Compozy-related prompts, reviews, workflow notes, and handoffs in Brazilian Portuguese.

## Principle

Do not generate PRD, TechSpec, or Compozy task artifacts unless the user explicitly asks outside this skill. Prepare inputs, validate outputs, and route to specialized skills.

## Decision Flow

1. If the user has no project idea, run `idea-discovery-assistant`.
2. If the user has an idea but no structured input for Compozy, run `compozy-input-brief`.
3. If the user is entering an existing repo, run `existing-codebase-onboarding`, then `design-docs-auditor`.
4. If Compozy artifacts already exist, run `compozy-artifact-reviewer` if available; otherwise review for ambiguity, missing validation, dependency gaps, and implementation risk.
5. Before implementation by an agent, run `implementation-readiness-check` if available; otherwise check `AGENTS.md`, commands, tests, env vars, contracts, risks, and task clarity.
6. For LLM/RAG/prompt-heavy features, route to `prompt-registry-and-evals` and `agent-harness-engineer`.

## Outputs

Always produce:

- recommended workflow path;
- skills to run next;
- missing context to collect;
- Compozy input readiness status;
- implementation readiness status;
- risks and blockers.

## Standard Workflows

### New Project Without Idea

```text
idea-discovery-assistant
-> compozy-input-brief
-> Compozy
-> artifact review
-> agent-harness-engineer
-> implementation
-> post-implementation review
```

### Existing Codebase

```text
existing-codebase-onboarding
-> design-docs-auditor
-> compozy-input-brief
-> Compozy
-> implementation readiness
-> implementation
```

### AI Feature

```text
compozy-input-brief
-> Compozy
-> prompt-registry-and-evals
-> agent-harness-engineer
-> implementation
```

