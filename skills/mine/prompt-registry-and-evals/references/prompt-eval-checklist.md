# Prompt Registry And Evaluation Checklist

## Prompt Metadata

- name and owner;
- purpose and category;
- model/provider assumptions;
- variables;
- expected output format;
- examples;
- version;
- changelog;
- eval dataset link;
- approval status.

## Evaluation

- golden examples;
- negative examples;
- deterministic checks for format/schema;
- human review rubric when subjective;
- comparative evaluation across prompt versions;
- precision/recall/F1 when classification or extraction applies;
- cost and latency tracking.

## RAG / Query Enrichment

- query reformulation strategy;
- retrieval criteria;
- source attribution;
- chunking assumptions;
- hallucination checks;
- fallback for low confidence.

## Team Governance

- prompts reviewed like code;
- prompt changes linked to eval results;
- production prompts versioned;
- rollback path documented.

