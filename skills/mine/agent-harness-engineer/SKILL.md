---
name: agent-harness-engineer
description: "Design and audit the operating harness for AI coding agents including worktrees, boundaries, artifacts, state, validation gates, rubrics, observability, degradation handling, and safe parallel execution. Use before agent implementation, parallel SDD execution, or when agents are producing inconsistent or unverifiable results."
---

# Agent Harness Engineer

Use this skill to turn agent execution from improvisation into a controlled engineering workflow.

## Workflow

1. Inspect the repo for agent instructions, commands, docs, tests, CI, and generated artifacts.
2. Run the bundled audit script when possible:

```bash
python skills/mine/agent-harness-engineer/scripts/harness_audit.py /path/to/repo --out /path/to/repo/harness-audit
```

3. Read `references/harness-checklist.md`.
4. Recommend mechanical guardrails and verification gates.

## Evaluate

- agent instructions: `AGENTS.md`, `CLAUDE.md`, `.cursor/rules`, `.codex`;
- isolated execution: branches, worktrees, feature boundaries;
- state and artifacts: docs, plans, reports, handoffs;
- validation: tests, lint, build, E2E, screenshots, smoke checks;
- rubrics: score-based quality gates for UI, code, docs, and LLM behavior;
- observability: logs, traces, failure summaries;
- degradation: retries, timeouts, fallback, stopping rules.

## Output

Produce a Brazilian Portuguese report with:

- current harness maturity;
- missing guardrails;
- recommended repo files;
- commands agents must run;
- quality gates;
- parallel execution guidance.
