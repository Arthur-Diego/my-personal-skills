---
name: design-docs-auditor
description: Audit software repositories for missing or weak Design Docs, PRDs, ADRs, engineering guidelines, architecture records, API contracts, operational docs, and project decision documentation. Use when asked to validate a new or existing codebase against Design Docs practices, identify documentation gaps before implementation, create a technical documentation checklist, review repo readiness, or produce a remediation plan for product/architecture/design documentation.
---

# Design Docs Auditor

Use this skill to analyze a repository as a documentation and design-readiness reviewer. The output must focus on actionable gaps: what exists, what is weak, what is missing, and what to create next.

## Workflow

1. Inspect the repository structure before judging it.
2. Run the bundled audit script when a filesystem repo is available:

```bash
python ~/.codex/skills/design-docs-auditor/scripts/audit_design_docs.py /path/to/repo --out /path/to/repo/design-docs-audit
```

3. Read the generated Markdown report and JSON summary.
4. Supplement the script result with codebase-aware observations from key files.
5. Produce a concise review ordered by risk and implementation value.

## What To Evaluate

Use `references/checklist.md` as the standard. Load it when producing a detailed audit, creating missing docs, or judging whether a repo satisfies Design Docs practices.

Core categories:

- Product intent: problem statement, goals, non-goals, users, workflows, acceptance criteria.
- Technical design: architecture, components, data flow, API contracts, state, integrations, alternatives.
- Decisions: ADRs or equivalent decision log with context, options, consequences, and status.
- Engineering guidelines: coding standards, testing strategy, review rules, branching/release conventions.
- Operational readiness: env vars, deployment, observability, security, data/privacy, rollback, runbooks.
- Traceability: links between PRD, Design Doc, tasks, code areas, tests, migrations, and releases.

## Output Shape

Lead with findings, not praise.

Use this structure:

```markdown
**Design Docs Audit**
- Score: X/100
- Coverage: strong/partial/weak
- Highest-risk gap: ...

**Findings**
1. [Severity] Gap - evidence from file/path - why it matters - recommended artifact.

**Recommended Artifacts**
- docs/prd.md: ...
- docs/design/<feature>.md: ...
- docs/adr/0001-<decision>.md: ...

**Next Steps**
1. ...
```

When asked to implement missing docs, create focused templates in the repo instead of broad generic documents.

## Guardrails

- Do not treat a README as sufficient design documentation unless it explicitly covers product intent, architecture, decisions, and operations.
- Do not require heavyweight documentation for tiny repos; scale recommendations to project size and risk.
- Distinguish absence of evidence from confirmed absence.
- Prefer existing repo conventions over imposing a new documentation structure.
- Avoid inventing product decisions. Mark unknowns as questions or placeholders.
