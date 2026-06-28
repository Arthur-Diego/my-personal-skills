---
name: compozy-input-brief
description: Convert a raw idea, meeting notes, codebase context, or vague request into a clean Compozy-ready input brief. Use before Compozy when the user needs structured context, constraints, and questions, but must not generate PRD, TechSpec, or SDD task files.
---

# Compozy Input Brief

Use this skill to prepare inputs for Compozy. Write all outputs in Brazilian Portuguese.

## Non-Goal

Do not create PRD, TechSpec, task breakdown, ADR, or SDD artifacts. Compozy owns those outputs.

## Workflow

1. Gather available context.
2. Separate known facts from assumptions.
3. Identify missing business and technical inputs.
4. Produce a concise brief that can be pasted into Compozy.
5. Include a short "perguntas abertas" section when critical inputs are missing.

## Template

Use `references/brief-template.md`.

## Quality Bar

- Clear enough for Compozy to generate artifacts.
- Honest about unknowns.
- Specific about user, problem, constraints, and desired outcome.
- Explicit about AI/LLM/RAG involvement, if any.

