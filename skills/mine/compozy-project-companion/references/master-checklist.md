# Master Project Context Checklist

Use this as the readiness checklist for `compozy-project-companion`.

Statuses:

- `complete`: enough evidence exists.
- `partial`: usable, but risk remains.
- `missing`: not found or not provided.
- `blocked`: cannot proceed without user or external action.
- `waived`: user explicitly accepted the risk.

## Gate 1 - Project Stage

Check:

- greenfield or brownfield;
- current phase: before Compozy, after Compozy, before implementation, after implementation;
- feature/task/wave boundary;
- whether the change is small, medium, or high risk.

GREEN requires clear stage and boundary.

## Gate 2 - Compozy Boundary

Check:

- Compozy has not been replaced by the skill;
- manual Compozy step is explicit when needed;
- Compozy input brief exists or is not needed;
- Compozy output artifacts are available when post-Compozy.

RED if the user expects the skill to generate PRD/TechSpec/tasks but no manual Compozy run happened.

## Gate 3 - Design Context

Check:

- goals and non-goals are known;
- relevant design docs exist or gaps are listed;
- ADRs exist for consequential decisions;
- API/event/schema contracts are documented when changed;
- operational constraints are known.

Route to `design-docs-auditor` if uncertain.

## Gate 4 - Brownfield Onboarding

Check for existing projects:

- stack;
- entrypoints;
- run/test/build commands;
- architecture/modules;
- APIs/routes;
- persistence/migrations;
- risks and first safe changes.

Route to `existing-codebase-onboarding` if missing.

## Gate 5 - Agent Harness

Check:

- `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, or equivalent;
- validation commands;
- branch/worktree strategy when needed;
- artifact/handoff location;
- failure handling;
- evidence required for completion.

Route to `agent-harness-engineer` if missing.

## Gate 6 - AI / Prompt / RAG

Check when feature uses IA:

- prompt ownership and versioning;
- evals or golden cases;
- model/provider assumptions;
- cost/latency constraints;
- hallucination/fallback strategy;
- RAG retrieval and source attribution, if applicable.

Route to `prompt-registry-and-evals` if missing.

## Gate 7 - Implementation Readiness

Check:

- task/wave is small enough;
- dependencies are clear;
- acceptance criteria are testable;
- tests or validation evidence are defined;
- environment/secrets are available or explicitly blocked.

RED if implementation cannot be verified.

## Gate 8 - Post-Implementation Context

Check after implementation:

- tests/build/lint ran or failure is documented;
- docs/ADRs/contracts updated if behavior changed;
- prompts/evals updated if IA changed;
- residual risks listed;
- next wave is identified.

YELLOW if validation could not fully run but risk is documented. RED if implementation changed behavior without evidence.

## Rerun Triggers

Run `compozy-project-companion` again when:

- a new feature begins;
- a new Compozy task wave begins;
- a feature wave ends;
- Compozy artifacts change;
- an agent is about to implement;
- an agent finished implementation;
- validation fails or cannot run;
- architecture, database, API contract, auth, deploy, prompts, RAG, evals, or operations change;
- the project context no longer matches current implementation;
- the next step is unclear.

Skip rerun only when the work is a small isolated task with clear validation and no impact on context, docs, contracts, or architecture.
