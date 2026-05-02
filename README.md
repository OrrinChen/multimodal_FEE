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

The local portfolio-ready MVP, real-retrieval hardening slice, Phase 9 portfolio case studies, Phase 10 investor-deck chart extraction slice, Phase 11 raw corpus indexing slice, Phase 12 embedding/reranking backend slice, Phase 13 validator-gated LLM decomposition slice, Phase 14 narrative/causal verification slice, Phase 15 adversarial/red-team evaluation slice, Phase 16 trace/reproducibility hardening slice, Phase 17 portfolio report artifact, and Phase 18 lightweight local demo UI are complete.

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
- pluggable embedding providers with deterministic offline default and optional local/live backends
- cached embedding index manifests
- metadata reranker interface and Phase 12 method report separating `dense_proxy` from optional `dense_real`
- validator-gated LLM claim decomposition interfaces
- recorded offline LLM decomposition fixtures for 5 complex financial claims
- schema validation for recorded LLM decomposition output
- entity, fiscal-period, and metric validator gates that reject hallucinated LLM subclaims
- rule-based versus recorded-LLM decomposition comparison artifacts
- an optional live LLM decomposer placeholder that is disabled by default and never required by tests
- narrative and causal claim verification with partial verdicts
- 10 narrative/causal due-diligence tasks covering numeric trends, segment contribution, causal attribution, management guidance, risk-factor changes, and deck narratives
- memo sections that separate evidence-supported numeric trends, inference, and unsupported causal attribution
- ordinary RAG overclaim reporting for causal/narrative failure cases
- adversarial/red-team task generation with 120 tasks across 12 failure modes
- failure-mode taxonomy and validator coverage matrix
- explainable failure reasons without requiring perfect full-engine accuracy
- SQLite-backed trace store with run, retrieval, verification, evidence, memo, and artifact manifests
- reproducibility trace artifacts for the three portfolio case studies
- case-study regeneration from trace records
- portfolio-ready report generator with Markdown, PDF, figure specs, table specs, resume bullet, and manifest artifacts
- lightweight local Streamlit demo over existing artifacts
- local claim-verification demo path that requires no API key
- Phase 0 through Phase 18 tests under `tests/`

The next recommended action is Phase 19: harden the local CLI and production workflow. The default dense retrieval path remains an offline deterministic token-vector proxy; real embedding and live LLM providers are optional and skipped gracefully when unavailable.

## Portfolio Case Studies

| Case | Failure mode | Claim | Full-engine verdict | Artifact |
| --- | --- | --- | --- | --- |
| `fiscal_period_confusion` | `period_confusion` | Apple's FY2024 revenue grew versus FY2023. | `support` | [Markdown](reports/case_studies/fiscal_period_confusion.md) |
| `numeric_unit_mismatch` | `numeric_validation_gap` | Apple's FY2024 operating margin exceeded Microsoft's FY2024 operating margin. | `support` | [Markdown](reports/case_studies/numeric_unit_mismatch.md) |
| `unsupported_narrative_claim` | `unsupported_claim` | Apple's FY2024 margin expansion was driven by durable operating leverage. | `insufficient` | [Markdown](reports/case_studies/unsupported_narrative_claim.md) |

See `ROADMAP.md` and `TASK_MEMORY.md` before starting work.

## LLM Decomposition Slice

Phase 13 keeps rule-based decomposition as the default, adds recorded LLM outputs as deterministic offline fixtures, and gates all LLM-generated subclaims through schema, entity, fiscal-period, and metric validation.

- JSON artifact: `experiments/llm_decomposition/phase13_decomposition_comparison.json`
- Markdown artifact: [phase13_decomposition_comparison.md](reports/llm_decomposition/phase13_decomposition_comparison.md)

## Narrative / Causal Verification Slice

Phase 14 prevents numeric or management-language support from being over-read as causal proof. It adds partial verdicts such as `support_numeric_only`, `support_narrative`, `contradict_numeric`, `contradict_narrative`, and `insufficient_causal_support`.

- JSON artifact: `experiments/narrative_causal/phase14_narrative_causal_report.json`
- Markdown artifact: [phase14_narrative_causal_report.md](reports/narrative_causal/phase14_narrative_causal_report.md)

## Red-Team Summary

Phase 15 adds adversarial evaluation instead of chasing perfect accuracy. The report contains 120 tasks across 12 failure modes, maps each mode to a validator owner, and keeps missed hard cases explainable.

- JSON artifact: `experiments/adversarial/phase15_adversarial_report.json`
- Markdown artifact: [phase15_adversarial_report.md](reports/adversarial/phase15_adversarial_report.md)

## Reproducibility Trace

Phase 16 records the case-study runs in a local SQLite trace store. Each run keeps a config hash, corpus version, method, task id, retrieved chunks, validator results, final verdict, runtime, and artifact paths.

One-command trace reproduction:

```bash
python3 scripts/smoke_trace_reproducibility.py
```

- SQLite trace DB: `experiments/traces/phase16_trace.sqlite`
- Artifact manifest: `reports/traces/phase16_artifact_manifest.json`

## Portfolio Report

Phase 17 builds the recruiter-facing technical artifact.

```bash
python3 scripts/build_portfolio_report.py
```

- PDF: [final_report.pdf](reports/final_report.pdf)
- Markdown: [final_report.md](reports/final_report.md)
- Manifest: `reports/portfolio_report_manifest.json`
- Resume bullet: `reports/resume_bullet.txt`

## Local Demo

Phase 18 adds a local demo UI over checked-in artifacts. It has four views: claim verification, case study browser, retrieval method comparison, and memo view.

```bash
python3 -m streamlit run app.py
```

Offline smoke checks:

```bash
python3 scripts/smoke_demo_ui.py
python3 scripts/smoke_streamlit_start.py
```
