---
name: compozy-project-companion
description: Master checklist and readiness checkpoint for Compozy-centered projects. Use before and after feature waves, when starting greenfield work, entering brownfield codebases, preparing Compozy input, validating Compozy output, deciding which companion skill to run, or checking if implementation by AI agents is GREEN, YELLOW, or RED. This skill does not run Compozy or generate PRD, TechSpec, or task artifacts.
---

# Compozy Project Companion

Use this skill as the master checklist for projects that use Compozy as the SDD source of truth. Write all Compozy-related prompts, reviews, workflow notes, checklist results, and handoffs in Brazilian Portuguese.

## Core Rule

Do not run Compozy. Do not generate PRD, TechSpec, or Compozy task artifacts. Prepare inputs, validate outputs, route to specialized skills, and decide whether implementation is ready.

## When To Use

Use this skill:

- at project start;
- before running Compozy;
- after Compozy generates or updates artifacts;
- before each significant feature or wave of tasks;
- after each feature wave;
- when a task changes architecture, API contracts, database, auth, deploy, prompts, RAG, or agent workflow;
- when an agent fails, expands scope, or produces unverifiable work;
- when the user is unsure which skill to run next.

Do not use for every small isolated task when the next action is obvious.

## When To Run Again

Run this skill again as a recurring checkpoint:

- before starting a new feature;
- before starting a new Compozy task wave;
- after finishing a feature wave;
- after Compozy artifacts are updated;
- before handing work to an AI coding agent;
- after an AI coding agent finishes implementation;
- when implementation changes architecture, database, API contracts, auth, deploy, prompts, RAG, evals, or agent workflow;
- when tests fail or validation cannot run;
- when the agent changes more files than expected;
- when docs, ADRs, contracts, prompts, or operations may be stale;
- when the next action is no longer obvious.

Do not run again for a tiny task that is isolated, has clear acceptance criteria, does not affect contracts/docs/architecture/prompts, and has an obvious validation command.

Use this rule:

```text
Obvious small task -> do not rerun.
Feature, wave, risk, ambiguity, failed validation, or changed context -> rerun.
```

## Modes

Choose one mode from context. If unclear, ask one short question.

- `route`: decide greenfield/brownfield/current-stage and next skills.
- `pre-compozy`: check whether the input for Compozy is ready.
- `post-compozy`: review Compozy outputs for implementation readiness.
- `pre-implementation`: decide if an agent can safely implement the next task/wave.
- `post-implementation`: validate whether context, docs, gates, and risks are still green.

## Readiness Semaforo

Return exactly one status:

- `GREEN`: implementation can proceed.
- `YELLOW`: can proceed with listed non-blocking risks or waived gaps.
- `RED`: do not implement yet; blocking context is missing.

## Required Checklist

Load `references/master-checklist.md` when doing a readiness checkpoint.

Evaluate:

1. Project stage and scope.
2. Compozy input/output readiness.
3. Design context readiness.
4. Agent harness readiness.
5. AI/prompt/RAG readiness, when applicable.
6. Implementation boundary.
7. Validation evidence.
8. Required next skills.

## Routing Rules

- No idea: run `idea-discovery-assistant`.
- Idea exists but is not structured for Compozy: run `compozy-input-brief`.
- Existing repo: run `existing-codebase-onboarding`, then `design-docs-auditor`.
- Missing/weak Design Docs, ADRs, contracts, or ops docs: run `design-docs-auditor`.
- Agent execution is risky or unclear: run `agent-harness-engineer`.
- Feature uses prompts, LLMs, RAG, LangChain, LangSmith, evals, or prompt versioning: run `prompt-registry-and-evals`.
- Legacy/refactoring focus: run `refactor-arch`.

## Output Format

Always produce:

```markdown
# Compozy Project Readiness

## Mode
...

## Status
GREEN | YELLOW | RED

## Decision
Pode implementar? Sim/Nao/Sim, com ressalvas.

## Checklist
| Gate | Status | Evidence | Missing |
| --- | --- | --- | --- |

## Skills To Run
1. ...

## Manual Steps
1. ...

## Blockers / Risks
- ...

## Next Action
...
```

## Definition Of Done

This skill is complete when it has:

- selected the correct mode;
- assigned GREEN/YELLOW/RED;
- listed missing context;
- identified required skills;
- separated automatic skill work from manual Compozy steps;
- produced a concrete next action.
