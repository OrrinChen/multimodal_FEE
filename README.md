# Multimodal Financial Due-Diligence Evidence Engine

This repository is a planning scaffold for a claim-level financial evidence verification engine.

The project goal is to verify financial due-diligence claims across SEC filings, XBRL facts, earnings transcripts, investor decks, tables, charts, and financial metrics without hallucinating evidence.

## Core Workflow

```text
financial claim
-> decompose subclaims
-> retrieve evidence
-> extract text/table/chart/XBRL support
-> normalize company, metric, period, unit, and currency
-> reconcile numbers
-> build evidence graph
-> detect unsupported or contradictory claims
-> produce auditable due-diligence memo
```

## Repository Control Files

- `AGENTS.md`: project-specific instructions for Codex and other coding agents
- `ROADMAP.md`: project phases, acceptance criteria, deferred work, and next action
- `TASK_MEMORY.md`: current status, decisions, completed work, validation results, and next steps
- `VALIDATION.md`: required validation and smoke-check commands
- `RUNBOOK.md`: common local commands and operating notes

## Current Status

Phase 7 is complete for the local deterministic evaluation and ablation slice.

The repository now includes:

- Python project metadata in `pyproject.toml`
- the initial 3-company universe in `configs/companies.yaml`
- package layout under `src/financial_evidence_engine/`
- SEC submissions and XBRL company facts metadata registry code
- source payload cache and stable version hashes
- SEC filing section splitting
- XBRL fact extraction into evidence units
- transcript speaker/section parsing
- markdown table numeric extraction
- entity, ticker, CIK, fiscal period, metric, unit, and currency normalization
- guardrails that reject accidental company, period, frequency, metric, currency, and unreconciled scale mismatches
- typed evidence graph nodes and edges for companies, documents, fiscal periods, metrics, claims, evidence units, risk themes, speakers, segments, and events
- graph builder from `DocumentMetadata` and `EvidenceUnit`
- claim-to-evidence, metric-to-evidence, company-period, and risk-theme graph query helpers
- claim and subclaim models
- deterministic claim decomposition for simple financial numeric claims
- graph-based evidence selection
- citation, fiscal-period, source-consistency, numeric, and unsupported-claim validators
- support / contradict / insufficient verdict generation
- typed due-diligence task models for evaluation gold labels
- a 60-task seed set across 10 companies and 6 due-diligence task families
- expected evidence units, numeric checks, allowed source types, verdicts, and known distractors for each task
- deterministic evaluation metrics for evidence recall, citation exactness, numeric correctness, fiscal-period correctness, entity correctness, verdict accuracy, contradiction detection, unsupported-claim rate, answer faithfulness, memo usefulness, latency, and cost
- six diagnostic baseline profiles: BM25 RAG, dense RAG, hybrid retrieval + reranker, GraphRAG only, multimodal extraction only, and full evidence engine
- six ablation profiles covering graph, numeric validator, fiscal-period validator, chart/table extraction, contradiction detector, and reranker removal
- Phase 0 through Phase 7 tests under `tests/`

The next recommended action is Phase 8: auditable due-diligence memo. Build the memo generator against the verified claim and evaluation outputs before adding UI or cloud deployment.

See `ROADMAP.md` and `TASK_MEMORY.md` before starting work.
