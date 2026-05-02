# Multimodal Financial Due-Diligence Evidence Engine

This repository is a claim-level financial evidence verification engine for due diligence.

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

The local portfolio-ready MVP, real-retrieval hardening slice, Phase 9 portfolio case studies, Phase 10 investor-deck chart extraction slice, and Phase 11 raw corpus indexing slice are complete.

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
- a local real-retrieval evaluation slice over a 320-document corpus built from gold evidence specs plus known distractors
- real BM25, deterministic token-vector dense proxy, hybrid, graph-constrained, and validator-augmented retrieval runs
- failure-case surfacing for period confusion, entity mismatch, citation mismatch, numeric validation gaps, missed contradictions, unsupported claims, and chart extraction gaps
- auditable due-diligence memo generation with executive summary, key claims, evidence table, numeric reconciliation, contradictions, risk flags, unresolved issues, limitations, and traceable conclusions
- markdown serialization that separates evidence from inference
- final report packaging with chart specs, result tables, sample memo, reproducibility commands, and polished resume bullets
- portfolio case studies that turn the real retrieval failures into recruiter-facing JSON and Markdown artifacts
- a minimal investor-deck PDF/chart extraction loop for one NVDA FY2024 chart fixture
- chart evidence conversion into traceable evidence units
- chart-to-XBRL reconciliation with insufficient verdicts when chart evidence is missing
- a 482-chunk raw corpus fixture with SEC filing sections/paragraphs, XBRL facts, transcript turns, deck pages, and deck chart units
- raw chunk provenance with company, source type, document id, fiscal period, section/page, text span, and stable hash
- retrieval evaluation corpus selection for `benchmark` versus `raw` corpus modes
- Phase 0 through Phase 11 tests under `tests/`

The next recommended action is Phase 12: add pluggable embedding and reranking backends while keeping deterministic offline defaults. The dense retrieval path is currently an offline deterministic token-vector proxy, not a neural embedding model or external vector database.

## Portfolio Case Studies

| Case | Failure mode | Claim | Full-engine verdict | Artifact |
| --- | --- | --- | --- | --- |
| `fiscal_period_confusion` | `period_confusion` | Apple's FY2024 revenue grew versus FY2023. | `support` | [Markdown](reports/case_studies/fiscal_period_confusion.md) |
| `numeric_unit_mismatch` | `numeric_validation_gap` | Apple's FY2024 operating margin exceeded Microsoft's FY2024 operating margin. | `support` | [Markdown](reports/case_studies/numeric_unit_mismatch.md) |
| `unsupported_narrative_claim` | `unsupported_claim` | Apple's FY2024 margin expansion was driven by durable operating leverage. | `insufficient` | [Markdown](reports/case_studies/unsupported_narrative_claim.md) |

See `ROADMAP.md` and `TASK_MEMORY.md` before starting work.
