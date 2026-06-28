# Agent Harness Checklist

## Required Repo Artifacts

- `AGENTS.md` or equivalent agent instructions.
- Clear setup/run/test commands.
- `.env.example` and environment documentation when env vars exist.
- Feature/task boundary conventions.
- Test and validation gates.
- Report or handoff location.

## Execution Control

- Prefer small, verifiable units.
- Use branches/worktrees for parallel work.
- State required commands before implementation.
- Define stop conditions: tests pass, evidence captured, blocker found.
- Require evidence for UI and external integration changes.

## Quality Gates

- Static: lint, typecheck, format.
- Functional: unit/integration/E2E/smoke tests.
- Documentation: docs updated when behavior changes.
- Contracts: API/schema changes documented.
- AI features: evals, prompt versions, fallback behavior.

## Failure Handling

- Distinguish environment failure from implementation failure.
- Record commands and errors.
- Avoid silent skips.
- Require explicit residual risk if validation cannot run.

