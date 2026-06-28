---
name: existing-codebase-onboarding
description: Analyze an existing repository so a developer or AI agent can safely enter the project. Use before Compozy or implementation work to map stack, architecture, entrypoints, modules, APIs, data storage, commands, tests, risks, documentation gaps, and first safe change boundaries.
---

# Existing Codebase Onboarding

Use this skill when entering an existing project. The goal is orientation and risk reduction, not refactoring.

## Workflow

1. Inspect files with `rg --files` and read manifests first.
2. Run the bundled scanner when a repository path is available:

```bash
python skills/mine/existing-codebase-onboarding/scripts/onboarding_scan.py /path/to/repo --out /path/to/repo/onboarding-report
```

3. Read the generated `onboarding.md`.
4. Supplement with focused source inspection.
5. Produce an onboarding report in Brazilian Portuguese.

## Evaluate

- stack and dependency managers;
- entrypoints;
- run/build/test commands;
- API routes and UI routes;
- data model and migrations;
- authentication and external services;
- tests and quality gates;
- docs and operational notes;
- risky areas and safe first changes.

## Output

Use `references/report-template.md`.

## Guardrails

- Do not edit code during onboarding.
- Distinguish facts from hypotheses.
- If commands are inferred, mark them as inferred.
- Prefer concrete paths and files.

