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

Phase 3 is complete for the local financial normalization slice.

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
- Phase 0, Phase 1, Phase 2, and Phase 3 tests under `tests/`

The next recommended action is Phase 4: evidence graph. Start with typed graph nodes and edges that connect companies, documents, fiscal periods, metrics, claims, and evidence units before retrieval or memo generation.

See `ROADMAP.md` and `TASK_MEMORY.md` before starting work.
