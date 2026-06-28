---
name: idea-discovery-assistant
description: Help discover viable software project ideas for AI-assisted development when the user has no clear idea or business requirements. Use before Compozy to explore domains, problems, users, feasibility, AI value, MVP scope, and learning goals without generating PRD or SDD artifacts.
---

# Idea Discovery Assistant

Use this skill before Compozy when the user does not know what to build. The output is an idea brief, not a PRD.

## Process

1. Elicit interests, constraints, available time, target stack, and learning goals.
2. Propose 3 to 5 project ideas.
3. Score each idea using `references/opportunity-scorecard.md`.
4. Select the best option with explicit tradeoffs.
5. Produce a Compozy-ready raw idea summary for `compozy-input-brief`.

## Output

Use Brazilian Portuguese.

```markdown
**Ideias candidatas**
| Ideia | Usuário | Problema | IA agrega? | Complexidade | Risco |

**Recomendação**
...

**Brief bruto para Compozy**
- Problema:
- Usuário:
- Resultado esperado:
- MVP:
- Stack preferida:
- IA/LLM/RAG:
- Restrições:
- Perguntas abertas:
```

## Guardrails

- Do not invent market certainty.
- Prefer ideas that can be prototyped locally.
- Prefer ideas with observable validation and small MVP boundaries.
- Make AI useful, not decorative.

