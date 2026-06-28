# Design Docs Audit Checklist

Use this checklist to evaluate whether a repository has enough design documentation to support implementation, maintenance, review, and future AI-assisted development.

## 1. Product Intent / PRD

Expected evidence:

- Problem statement and context.
- Goals and non-goals.
- Target users or actors.
- User journeys or workflow descriptions.
- Functional requirements.
- Non-functional requirements.
- Acceptance criteria.
- Rollout or release constraints.
- Open questions.

Weak signals:

- README only explains installation.
- Requirements live only in issue titles or chat history.
- No explicit non-goals.
- No acceptance criteria.

Recommended artifact:

- `docs/prd.md`
- `docs/prd/<feature>.md`
- existing product/spec folder if the repo already has one.

## 2. Technical Design / Design Doc

Expected evidence:

- Proposed architecture and boundaries.
- Component responsibilities.
- Data model and storage choices.
- API contracts, events, queues, or integration contracts.
- Sequence/data-flow diagrams or prose equivalents.
- Alternatives considered.
- Tradeoffs and constraints.
- Failure modes.
- Migration/backward compatibility plan.
- Testing strategy tied to the design.

Weak signals:

- Architecture implied only by code.
- No explanation of why the current design exists.
- API contracts only visible in handlers/controllers.
- No migration or compatibility notes for schema changes.

Recommended artifact:

- `docs/design/<feature-or-system>.md`
- `docs/architecture.md`
- `docs/contracts/*.md`

## 3. Decision Records / ADRs

Expected evidence:

- Decision log for consequential choices.
- Status: proposed, accepted, superseded, deprecated.
- Context and problem.
- Options considered.
- Decision and consequences.
- Links to PRDs, design docs, issues, or code.

Weak signals:

- Commit messages are the only decision history.
- No record of alternatives.
- Major framework, database, or deployment choices lack rationale.

Recommended artifact:

- `docs/adr/0001-title.md`
- `docs/decisions/*.md`

## 4. Engineering Guidelines

Expected evidence:

- Coding conventions.
- Test expectations.
- Review standards.
- Branching/release flow.
- Dependency policy.
- AI-agent or automation instructions, when relevant.
- Definition of done.

Weak signals:

- Only formatter/linter config exists.
- No test strategy.
- No contribution/review instructions.
- No local development troubleshooting.

Recommended artifact:

- `AGENTS.md`
- `CONTRIBUTING.md`
- `docs/engineering-guidelines.md`
- `docs/testing.md`

## 5. Operational Readiness

Expected evidence:

- Environment variables and secrets documentation.
- Local runbook.
- Deployment steps.
- Observability/logging/metrics notes.
- Security and privacy considerations.
- Backup/restore or data retention notes when stateful.
- Rollback plan.
- Incident/runbook guidance for production systems.

Weak signals:

- `.env.example` exists but variables are unexplained.
- Deployment is tribal knowledge.
- No health checks or troubleshooting notes.
- No security notes despite auth, payments, PII, or external integrations.

Recommended artifact:

- `docs/operations.md`
- `docs/deployment.md`
- `docs/runbook.md`
- `.env.example` with comments or companion docs.

## 6. Traceability

Expected evidence:

- Docs link to code modules, tasks, tests, migrations, or APIs.
- Design docs reference PRDs.
- ADRs reference design docs or issues.
- Tests map to acceptance criteria or major flows.

Weak signals:

- Docs exist but are disconnected from implementation.
- No owner/status/date.
- No way to tell which design applies to current code.

Recommended artifact:

- Add frontmatter or metadata to docs.
- Add "Related code", "Related tests", and "Decision links" sections.

## Severity Guide

- Critical: Missing docs create high risk for implementation, security, data loss, compliance, or production operation.
- High: Missing docs likely cause wrong architecture, rework, onboarding failure, or brittle AI-generated changes.
- Medium: Missing docs reduce maintainability or review quality but do not block immediate progress.
- Low: Useful improvement, cleanup, naming, or traceability gap.
