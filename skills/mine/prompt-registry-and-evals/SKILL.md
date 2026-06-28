---
name: prompt-registry-and-evals
description: Design or audit prompt registries, prompt versioning, prompt.yaml metadata, prompt tests, comparative evaluations, query reformulation, prompt enrichment, and quality gates for LLM applications or team productivity prompts. Use when a project uses prompts in production, agents, RAG, LangChain/LangSmith, or shared AI workflows.
---

# Prompt Registry And Evals

Use this skill to manage prompts as engineering artifacts rather than loose text.

## Workflow

1. Identify prompt categories: productivity, agent workflow, application runtime, RAG/query enrichment, eval prompts.
2. Inspect existing prompt files, LangSmith references, YAML metadata, tests, and eval datasets.
3. Run the bundled checker when possible:

```bash
python skills/mine/prompt-registry-and-evals/scripts/prompt_registry_check.py /path/to/repo --out /path/to/repo/prompt-registry-audit
```

4. Use `references/prompt-eval-checklist.md` to recommend structure and gates.

## Recommend

- `prompts/<domain>/<name>/prompt.md`;
- `prompts/<domain>/<name>/prompt.yaml`;
- examples/golden cases;
- eval script or LangSmith dataset;
- versioning and review rules;
- cost/latency/quality metrics.

## Output

Write in Brazilian Portuguese:

- current prompt maturity;
- missing registry structure;
- eval strategy;
- suggested prompt metadata;
- quality gates and next steps.

