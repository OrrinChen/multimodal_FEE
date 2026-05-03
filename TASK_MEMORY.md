# Task Memory: Multimodal Financial Due-Diligence Evidence Engine

## Latest Status

Current branch:

```text
codex/financial-evidence-release-packaging
```

Latest commit:

```text
docs: add release assets and portfolio pitch
```

Current phase:

```text
Phase 20 complete: Final Resume / Interview Packaging
```

Main blocker:

```text
None. The current roadmap is complete through Phase 20.
```

Next recommended action:

```text
Use the portfolio report, local demo, and interview docs for applications. Future work should be driven by interview feedback or a new roadmap, not by adding generic features.
```

Latest workflow update:

```text
Prepared release packaging after the public portfolio freeze audit.

Added:
- README top visual strip with three portfolio screenshots
- scripts/build_portfolio_screenshots.py for deterministic local screenshot asset generation
- docs/assets/claim_verification_demo.png
- docs/assets/case_study_replay.png
- docs/assets/memo_trace_demo.png
- docs/sixty_second_pitch.md with English and Chinese pitch scripts
- portfolio screenshot build command in README/VALIDATION/RUNBOOK/report reproducibility commands
```

Latest validation:

```text
Passed:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest: 100 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check: companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check: sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check: company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check: nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check: verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check: tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check: tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check: tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check: case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check: deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check: raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check: tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check: methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check: complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check: narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check: adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check: runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase17 portfolio report build check: sections=10 pages=10 case_studies=3 figures=5 tables=3 pdf=reports/final_report.pdf markdown=reports/final_report.md manifest=reports/portfolio_report_manifest.json
- phase18 demo UI smoke check: pages=4 case_studies=3 methods=5 local_claim_verdict=support api_key_required=False app=app.py
- phase18 Streamlit start smoke check: streamlit_started=True url=http://127.0.0.1:54900 app=app.py
- phase19 CLI workflow smoke check: commands=6 verify_verdict=support raw_chunks=482 eval_tasks=60 case_studies=3 report_pages=10 serve_demo=True network_enabled=False
- phase20 interview packaging smoke check: docs=6 readme_2min=True report_10min=True repo_30min=True evidence_framing=True
- portfolio screenshot build check: screenshots=3 claim=docs/assets/claim_verification_demo.png case=docs/assets/case_study_replay.png memo=docs/assets/memo_trace_demo.png
- public portfolio freeze audit test: 3 passed
- phase8 memo smoke check: verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check: tasks=60 charts=4 tables=3 commands=27 sample_memo_verdict=support markdown_lines=144

Skipped:
- none
```

## Completed Phases

### Phase 0: Planning and Repository Skeleton

Commit:

```text
Phase 0 skeleton commit in this repository history.
```

What changed:

```text
Created the repository automation workflow, Python package skeleton, initial 3-company universe, validation commands, and Phase 0 tests.
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase0_skeleton.py -q initially failed because pyproject.toml, configs/companies.yaml, and financial_evidence_engine were missing.
- After implementation, python3 -m pytest passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
```

Known limitations:

```text
No SEC data ingestion, document registry, cache, extraction, retrieval, evidence graph, validators, or memo generation are implemented yet.
```

### Phase 1: SEC/XBRL Document Registry and Ingestion

Commit:

```text
Phase 1 document registry commit in this repository history.
```

What changed:

```text
Implemented the local SEC/XBRL document registry slice for the initial company universe.
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase1_document_registry.py -q initially failed because document_registry, cache, sec_client, ingestion, and CompanyUniverseIndex were missing.
- After implementation, the Phase 1 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
```

Known limitations:

```text
SEC client supports public endpoints but final validation uses offline fixtures to avoid depending on network availability.
FMP transcript ingestion remains deferred because it requires paid/external service approval.
Investor deck registry remains deferred until SEC/XBRL extraction is stable.
No evidence unit extraction, text parsing, graph construction, validators, or memo generation are implemented yet.
```

### Phase 2: Text / Table / XBRL / Transcript Extraction

Commit:

```text
Phase 2 extraction commit in this repository history.
```

What changed:

```text
Implemented the local extraction layer that converts filing text, XBRL company facts, transcript text, and markdown tables into traceable evidence units.
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase2_extraction.py -q initially failed because text_extractor, xbrl_extractor, transcript_parser, and table_extractor were missing.
- After implementation, the Phase 2 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
```

Known limitations:

```text
Filing text extraction handles HTML/text fixtures and SEC item section splitting, but not full PDF binary extraction.
Transcript parsing works from supplied transcript text; FMP transcript ingestion remains deferred pending paid/external API approval.
Table extraction supports markdown-style tables only.
Chart extraction and investor deck parsing remain deferred.
No financial normalization guardrails, retrieval, graph construction, validators, or memo generation are implemented yet.
```

### Local FMP Snapshot: 2026-04-30

Commit:

```text
Not committed. Raw paid FMP payloads are stored locally under ignored data/cache/fmp/.
```

What changed:

```text
Captured a broad FMP local cache for AAPL, MSFT, NVDA, AMZN, GOOGL, META, JPM, WMT, TSLA, and NFLX.

Snapshot includes:
- transcripts and transcript dates for 2022-2025
- annual and quarterly financial statements
- annual and quarterly as-reported statements
- key metrics, ratios, enterprise values, growth metrics, financial scores, and owner earnings
- DCF and levered DCF payloads
- ratings snapshot/history, grades history, and grades consensus
- dividends, splits, market capitalization history, shares float, peers, executives, and employee counts
- analyst estimates, price targets, earnings calendar, stock news, and segment revenue
- historical daily prices from 2022-01-01 to 2026-04-30
```

Validation:

```text
Passed:
- manifest_records=700
- payload_json_files=700
- metadata_files=700
- 10 symbols with 70 payload groups each
- remaining_failures=0
- no apikey or FMP_API_KEY strings found in data/cache/fmp
- data/cache/fmp is ignored by git
```

Known limitations:

```text
FMP remains a secondary source, not the filing authority.
SEC/XBRL should remain the validator authority when numbers conflict.
Real-time quotes were intentionally not downloaded.
The cache is broad enough for offline MVP development, but future tasks outside the 10-symbol universe or after 2026-04-30 may require additional data.
```

### Phase 3: Financial Normalization Layer

Commit:

```text
feat: add financial normalization guardrails
```

What changed:

```text
Implemented a focused normalization layer that prevents common financial evidence mistakes before retrieval or graph reasoning.

Added:
- canonical NormalizedCompany, FiscalPeriod, and NormalizedAmount models
- ticker / CIK / company-name entity resolver
- fiscal vs calendar period resolver with annual-vs-quarterly guardrails
- period end date handling from DocumentMetadata
- metric alias mapper for revenue, total net sales, operating income, EBIT, net income, earnings, and operating cash flow
- currency normalization for USD/$ and common currency labels
- unit scale normalization for ones, thousands, millions, and billions
- FinancialObservation guardrails for company, metric, period, currency, and unreconciled scale mismatch
- Phase 3 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase3_normalization.py -q initially failed because the Phase 3 modules did not exist.
- After implementation, the Phase 3 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
```

Known limitations:

```text
Normalization currently covers the initial MVP metric and unit aliases, not a full XBRL taxonomy.
Fiscal period parsing supports common FY/CY and Q1-Q4 labels, not every natural-language period phrase.
Currency conversion rates are intentionally not implemented; the guardrail rejects currency mismatches instead of converting them.
Graph construction, claim verification, numeric reconciliation, and memo generation remain unimplemented.
```

### Phase 4: Evidence Graph

Commit:

```text
feat: add evidence graph builder
```

What changed:

```text
Implemented the first local evidence graph layer that connects documents, evidence units, metrics, claims, fiscal periods, companies, and risk themes.

Added:
- GraphNode and GraphEdge models
- NodeType and EdgeType constants for the roadmap graph schema
- EvidenceGraph in-memory container with deterministic insertion and duplicate-edge protection
- graph builder from DocumentMetadata and EvidenceUnit
- ClaimLink model for explicit support / contradiction links
- metric-to-evidence aggregation
- company-period evidence aggregation
- risk-theme evidence tracking across fiscal years
- Phase 4 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase4_evidence_graph.py -q initially failed because the Phase 4 graph interfaces did not exist.
- After implementation, the Phase 4 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
```

Known limitations:

```text
The graph is an in-memory local structure, not a persistent graph database.
Claim links are explicit inputs; automatic claim decomposition and evidence selection are not implemented yet.
Risk-theme tracking is keyword-based for now.
GraphRAG retrieval, validators, contradiction detection, and memo generation remain unimplemented.
```

### Phase 5: Claim Decomposition and Verification

Commit:

```text
feat: add claim verification engine
```

What changed:

```text
Implemented the first deterministic claim verification layer.

Added:
- Claim, Subclaim, EvidenceReference, ValidatorCheck, SubclaimVerification, and ClaimVerificationResult models
- Verdict labels: support, contradict, insufficient
- ClaimDecomposer for simple MVP numeric financial claims
- EvidenceSelector that selects graph evidence by company, fiscal period, metric, and required terms
- CitationValidator
- FiscalPeriodValidator
- SourceConsistencyValidator
- NumericValidator
- UnsupportedClaimDetector
- ClaimVerifier orchestration
- ContradictionDetector helper
- Phase 5 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase5_claim_verification.py -q initially failed because the Phase 5 reasoning and validator interfaces did not exist.
- After implementation, the Phase 5 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
```

Known limitations:

```text
Claim decomposition is deterministic and handles simple MVP numeric financial claims only.
Evidence selection is graph/metadata based, not semantic retrieval.
Numeric reconciliation uses exact value comparison unless tolerance is set on the subclaim.
Contradiction detection currently relies on failed validator checks, especially numeric mismatch.
Due-diligence task set, evaluation baselines, memo generation, and LLM-assisted decomposition remain unimplemented.
```

### Phase 6: Multimodal Due-Diligence Task Set

Commit:

```text
feat: add due diligence task set
```

What changed:

```text
Implemented the first evaluation gold-task layer for due-diligence verification.

Added:
- EvidenceRequirement, NumericCheckSpec, KnownDistractor, DueDiligenceTask, and DueDiligenceTaskSet models
- build_seed_task_set() with 60 tasks across 10 companies and 6 task families
- multi-hop / multi-document task checks
- validator-readable numeric-check labels for every task
- expected evidence, allowed source types, verdict labels, and known distractors for every task
- evaluation.yaml metadata for the seed task set
- Phase 6 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase6_task_set.py -q initially failed because build_seed_task_set did not exist.
- After implementation, the Phase 6 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
```

Known limitations:

```text
The Phase 6 task set is a gold specification layer, not a fully populated extracted-evidence corpus.
Investor-deck chart tasks specify required chart evidence, but chart extraction remains deferred.
Expected numeric checks identify validator intent, but Phase 7 metrics and baselines still need implementation.
```

### Phase 7: Evaluation and Ablations

Commit:

```text
feat: add evaluation and ablation harness
```

What changed:

```text
Implemented a deterministic evaluation harness over the Phase 6 gold task specs.

Added:
- RetrievedEvidence, TaskPrediction, EvaluationRun, and EvaluationReport models
- evidence recall@k, citation exactness, numeric correctness, fiscal-period correctness, entity correctness, unsupported-claim rate, contradiction detection accuracy, verdict accuracy, answer faithfulness, memo usefulness, latency, and cost metrics
- diagnostic baseline profiles for BM25 RAG, dense RAG, hybrid retrieval + reranker, GraphRAG only, multimodal extraction only, and full evidence engine
- ablation profiles for removing graph retrieval, numeric validator, fiscal-period validator, chart/table extraction, contradiction detector, and reranker
- Phase7EvaluationReport with acceptance findings
- Phase 7 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase7_evaluation.py -q initially failed because the Phase 7 evaluation interfaces did not exist.
- After implementation, the Phase 7 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
```

Known limitations:

```text
The Phase 7 baselines are deterministic diagnostic profiles over gold task specs, not production retriever implementations.
BM25, dense, hybrid, and GraphRAG profiles demonstrate expected failure modes but do not yet execute real document search.
Latency and cost metrics are profile-level placeholders for local evaluation, not measured service telemetry.
Memo generation, final report packaging, and LLM-assisted decomposition remain unimplemented.
```

### Phase 8: Auditable Due-Diligence Memo

Commit:

```text
feat: add auditable due diligence memo
```

What changed:

```text
Implemented the auditable memo layer that turns verified claims into a structured due-diligence artifact.

Added:
- DueDiligenceMemo, MemoClaim, MemoConclusion, EvidenceTableRow, NumericReconciliationRow, and MemoIssue models
- build_due_diligence_memo() for ClaimVerificationResult inputs
- executive summary, key claims, evidence table, numeric reconciliation, contradiction, risk flag, unsupported-claim, and limitation sections
- conclusion-level citation, source document, page/section, metric, period, validator result, evidence summary, and inference fields
- markdown rendering that keeps evidence and inference separate
- Phase 8 smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_phase8_memo.py -q initially failed because build_due_diligence_memo did not exist.
- After implementation, the Phase 8 test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
```

Known limitations:

```text
The memo generator currently consumes deterministic claim verification outputs; it does not write a polished PDF or notebook report.
The sample smoke memo uses local fixture evidence, not the full 60-task corpus.
Charts, final report narrative, reproducibility guide, and resume bullet packaging remain incomplete.
```

### Final Report and Reproducibility Package

Commit:

```text
feat: package final report artifacts
```

What changed:

```text
Packaged the local MVP into a final report artifact generator.

Added:
- FinalReportPackage, ChartSpec, and ReportTable models
- build_final_report_package() for Phase7EvaluationReport and DueDiligenceMemo inputs
- final report Markdown rendering with the 12-section report outline
- chart specs for citation correctness, numeric mismatch rate, unsupported-claim rate, and period-confusion errors
- baseline and ablation result tables
- reproducibility command table
- embedded sample due-diligence memo
- long and short resume bullets
- final report smoke script and validation command
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_final_report_package.py -q initially failed because build_final_report_package did not exist.
- After implementation, the final report package test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=12 sample_memo_verdict=support markdown_lines=122
```

Known limitations:

```text
The final report package is a deterministic Markdown/data artifact generator, not a designed PDF deck.
Charts are portable chart specs, not rendered image files.
The final report baseline tables still summarize Phase 7 diagnostic profiles; real retrieval execution is reported through the separate hardening slice.
```

### Real Retrieval Evaluation Hardening

Commit:

```text
feat: add real retrieval evaluation slice
```

What changed:

```text
Replaced the next-stage baseline gap with a local real-retrieval evaluation path that searches actual corpus documents instead of emitting only profile-level predictions.

Added:
- RetrievalCorpusDocument, RetrievalCorpus, RetrievalResult, RetrievalFailureCase, and RealRetrievalEvaluationResult models
- build_retrieval_corpus() with gold evidence documents and known distractors from the 60-task seed set
- BM25EvidenceRetriever with local BM25 scoring
- DenseEvidenceRetriever as an offline deterministic token-vector cosine proxy
- HybridEvidenceRetriever with BM25/vector score blending and metadata reranking
- GraphEvidenceRetriever with company, period, source-type, and metric constraints
- run_real_retrieval_evaluation() producing EvaluationRun, EvaluationReport, retrieved evidence, method notes, and failure cases
- smoke_real_retrieval_evaluation.py and tests for corpus construction, ranking, metrics, serialization, and failure-case surfacing
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_real_retrieval_evaluation.py -q initially failed because real retrieval APIs did not exist.
- After implementation, the real retrieval test file passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_documents=320 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=12 sample_memo_verdict=support markdown_lines=122
```

Known limitations:

```text
The real retrieval corpus is a local benchmark built from task evidence specs and known distractors, not raw SEC filing paragraphs or PDF pages.
The dense retriever is a deterministic token-vector proxy, not a neural embedding model.
GraphRAG is represented by metadata-constrained retrieval over the local corpus, not a production graph database.
The full-engine real run intentionally fails investor-deck chart tasks because chart/PDF extraction is still deferred.
```

### Phase 9: Portfolio Case Study Layer

Commit:

```text
feat: add portfolio case studies for retrieval failures
```

What changed:

```text
Turned the real retrieval benchmark into recruiter-facing case studies.

Added:
- case-study package under src/financial_evidence_engine/case_studies/
- PortfolioCaseStudy, MethodCaseResult, EvidenceReference, ValidatorCheck, and CaseStudyArtifactManifest models
- deterministic case selection from run_real_retrieval_evaluation()
- fiscal_period_confusion, numeric_unit_mismatch, and unsupported_narrative_claim cases
- JSON artifacts under experiments/case_studies/
- Markdown artifacts and index under reports/case_studies/
- README case-study summary
- scripts/smoke_case_studies.py
- tests/test_case_studies.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_case_studies.py -q initially failed because the case_studies package did not exist.
- After implementation, tests/test_case_studies.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_documents=320 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=14 sample_memo_verdict=support markdown_lines=124
```

Known limitations:

```text
Case studies are generated from the current 320-document local retrieval benchmark, not raw filing paragraphs or PDF pages.
The numeric/unit mismatch case currently reflects numeric validator failure in the local benchmark rather than a raw extracted unit-scale error.
Investor-deck PDF/chart extraction is covered by the Phase 10 minimal fixture slice; broad chart extraction remains deferred.
```

### Phase 10: Investor Deck PDF / Chart Extraction Slice

Commit:

```text
feat: add investor deck chart evidence extraction
```

What changed:

```text
Added a minimal but traceable investor-deck chart verification loop.

Added:
- DeckDocumentMetadata, DeckPage, ChartEvidenceUnit, ChartExtractionResult, ChartReconciliationRow, ChartVerificationIssue, and DeckChartVerificationResult models
- tests/fixtures/investor_decks/nvda_fy2024_data_center_chart.pdf
- extract_deck_chart_evidence() for text-extractable local PDF fixtures
- ChartEvidenceUnit.to_evidence_unit()
- reconcile_chart_evidence() against XBRL or filing evidence units
- verify_deck_chart_claim() with support / contradict / insufficient verdicts
- build_deck_chart_gap_task() without changing the 60-task seed set
- scripts/smoke_deck_chart_extraction.py
- tests/test_deck_chart_extraction.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_deck_chart_extraction.py -q initially failed because deck/chart extraction APIs did not exist.
- After implementation, tests/test_deck_chart_extraction.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_documents=320 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=14 sample_memo_verdict=support markdown_lines=124
```

Known limitations:

```text
The PDF fixture is text-extractable and deterministic; this is not a universal PDF parser.
The chart extractor reads explicit key/value chart lines rather than visual geometry.
Only one NVDA FY2024 investor-deck chart case is covered.
At Phase 10 completion, raw deck pages were not indexed into a raw corpus; Phase 11 now indexes the fixture deck page and chart chunks.
```

### Phase 11: Raw Filing Paragraph / Page Corpus

Commit:

```text
feat: add raw financial document corpus indexing
```

What changed:

```text
Added a deterministic raw-corpus indexing layer next to the existing 320-document benchmark corpus.

Added:
- ChunkProvenance, DocumentChunk, ChunkIndexManifest, CorpusVersionManifest, RawFinancialCorpus, and RawCorpusBuilder
- 482 raw chunks versus 320 curated benchmark documents
- SEC filing section chunks and paragraph chunks for 10 companies
- XBRL fact chunks, transcript-turn chunks, and filing-table chunks
- Phase 10 investor-deck page and chart chunks
- raw chunk hashes and source hashes for reproducibility
- raw chunk adapter into the existing RetrievalCorpusDocument interface
- `run_real_retrieval_evaluation(..., corpus_mode="benchmark"|"raw")`
- `scripts/smoke_raw_corpus.py`
- `scripts/smoke_real_retrieval_evaluation.py --corpus raw`
- tests/test_raw_corpus.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_raw_corpus.py -q initially failed because build_raw_financial_corpus and raw corpus mode did not exist.
- After implementation, tests/test_raw_corpus.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=15 sample_memo_verdict=support markdown_lines=125
```

Known limitations:

```text
The raw corpus is a deterministic local fixture, not a downloaded full SEC archive.
SEC filing paragraphs are source-like generated fixtures used to test chunking and provenance boundaries.
Only the NVDA Phase 10 deck fixture contributes real deck page/chart chunks.
At Phase 11 completion, raw corpus retrieval used deterministic BM25/token-vector/graph retrievers; Phase 12 now adds a pluggable embedding and reranking interface while keeping deterministic defaults.
```

### Phase 12: Pluggable Embedding / Reranking Backend

Commit:

```text
feat: add pluggable embedding and reranking backend
```

What changed:

```text
Added an offline-safe embedding and reranking backend layer.

Added:
- EmbeddingProvider protocol
- DeterministicTokenEmbeddingProvider for default offline proxy embeddings
- LocalSentenceTransformerProvider disabled by default with graceful skip
- OpenAIEmbeddingProvider disabled by default with graceful skip
- EmbeddingIndex and EmbeddingIndexManifest with JSON cache files
- EmbeddingEvidenceRetriever
- EmbeddingHybridEvidenceRetriever
- Reranker protocol
- MetadataBoostReranker
- EmbeddingRetrievalEvaluationResult
- run_embedding_retrieval_evaluation()
- scripts/smoke_embedding_backend.py
- tests/test_embedding_backend.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_embedding_backend.py -q initially failed because embedding provider, cache index, reranker, and embedding retrieval report APIs did not exist.
- After implementation, tests/test_embedding_backend.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=16 sample_memo_verdict=support markdown_lines=128
```

Known limitations:

```text
The default embedding path remains deterministic token hashing, not a neural embedding model.
Local sentence-transformers and OpenAI providers are adapters only; they are disabled by default and skipped when dependencies or keys are missing.
No external vector database is used; EmbeddingIndex is a local JSON cache.
Optional real embedding metrics are only present when a real provider is explicitly enabled.
```

### Phase 13: Validator-Gated LLM Claim Decomposition

Commit:

```text
feat: add validator-gated LLM claim decomposition
```

What changed:

```text
Added an offline, validator-gated LLM decomposition slice without making live LLMs authoritative or required.

Added:
- ClaimDecompositionProvider protocol
- RuleBasedClaimDecomposer for the existing deterministic decomposer
- RecordedLLMClaimDecomposer using local fixture outputs
- OptionalLiveLLMClaimDecomposer disabled by default
- DecompositionCandidate and DecompositionTrace
- ValidatorGate for entity, fiscal-period, and metric validation
- DecompositionComparisonReport and artifact writer
- 5 complex recorded LLM decomposition fixtures
- experiments/llm_decomposition/phase13_decomposition_comparison.json
- reports/llm_decomposition/phase13_decomposition_comparison.md
- scripts/smoke_llm_decomposition.py
- tests/test_llm_decomposition.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_llm_decomposition.py -q initially failed because the LLM decomposition provider, schema error, validator gate, comparison report, and live decomposer APIs did not exist.
- After implementation, tests/test_llm_decomposition.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=17 sample_memo_verdict=support markdown_lines=130
```

Known limitations:

```text
Recorded LLM decompositions are deterministic fixtures, not live model calls.
The live LLM decomposer is intentionally disabled by default and has no configured backend.
ValidatorGate checks allowed ticker, period, and metric vocabularies; Phase 14 adds a separate deterministic narrative/causal verifier for deeper semantic claims.
The comparison report measures decomposition coverage, not final narrative truth.
```

### Phase 14: Narrative / Causal Claim Verification

Commit:

```text
feat: add narrative and causal claim verification
```

What changed:

```text
Added a deterministic narrative/causal verification slice that prevents numeric or management-language evidence from being over-read as causal proof.

Added:
- ClaimType labels for numeric trend, segment contribution, causal attribution, management guidance, risk-factor change, and deck narrative claims
- PartialVerdict labels: support_numeric_only, support_narrative, contradict_numeric, contradict_narrative, and insufficient_causal_support
- NarrativeEvidenceFinding, NarrativeCausalTask, and NarrativeCausalTaskSet
- NarrativeCausalVerifier
- NarrativeCausalMemo with separate sections for evidence-supported numeric trend, inference, and unsupported causal attribution
- NarrativeCausalReport with ordinary RAG overclaim examples
- experiments/narrative_causal/phase14_narrative_causal_report.json
- reports/narrative_causal/phase14_narrative_causal_report.md
- scripts/smoke_narrative_causal.py
- tests/test_narrative_causal_verification.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_narrative_causal_verification.py -q initially failed because ClaimType, PartialVerdict, NarrativeCausalVerifier, task-set builder, memo/report builders, and artifact writer APIs did not exist.
- After implementation, tests/test_narrative_causal_verification.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=18 sample_memo_verdict=support markdown_lines=132
```

Known limitations:

```text
Phase 14 uses deterministic local task specs rather than live document retrieval for narrative causality.
The ordinary RAG verdicts are diagnostic labels for overclaim analysis, not model-generated live outputs.
The verifier checks explicit finding categories and statuses; broader adversarial coverage is handled by the separate Phase 15 red-team layer.
No live LLM or external service is required.
```

### Phase 15: Adversarial / Red-Team Evaluation

Commit:

```text
feat: add adversarial financial evidence evaluation
```

What changed:

```text
Added a deterministic adversarial/red-team evaluation layer for reliability-oriented testing.

Added:
- ADVERSARIAL_FAILURE_MODES with 12 financial evidence failure families
- FailureModeTaxonomy and FailureModeTaxonomyEntry
- AdversarialTask, AdversarialTaskSet, and AdversarialTaskGenerator
- AdversarialTaskResult and ValidatorCoverageReport
- 120 generated tasks across 10 companies and 12 failure modes
- validator coverage matrix across 11 validator owners
- non-perfect full-engine diagnostic accuracy to surface hard cases honestly
- experiments/adversarial/phase15_adversarial_report.json
- reports/adversarial/phase15_adversarial_report.md
- scripts/smoke_adversarial_evaluation.py
- tests/test_adversarial_evaluation.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_adversarial_evaluation.py -q initially failed because the adversarial task generator, failure-mode taxonomy, coverage report, and artifact writer APIs did not exist.
- After implementation, tests/test_adversarial_evaluation.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=19 sample_memo_verdict=support markdown_lines=134
```

Known limitations:

```text
Phase 15 tasks are deterministic local red-team fixtures, not generated from live retrieval failures.
The full-engine accuracy is diagnostic and intentionally not perfect; hard cases remain for wrong-segment, deck-only, and transcript-only claims.
Validator ownership is modeled in the taxonomy; concrete production validators for every owner are deferred to later hardening phases.
```

### Phase 16: Evidence Trace and Reproducibility Hardening

Commit:

```text
feat: add reproducible evidence trace manifests
```

What changed:

```text
Added a local reproducibility trace layer for the portfolio case studies.

Added:
- RunManifest, RetrievalTrace, VerificationTrace, EvidenceTrace, MemoTrace, and ArtifactManifest
- EvidenceTraceBundle for grouping trace records
- TraceStore backed by SQLite
- deterministic config hashes and corpus version records
- retrieved chunk, validator result, final verdict, runtime, and artifact-path records for each case-study run
- case-study regeneration from trace records
- experiments/traces/phase16_trace.sqlite
- reports/traces/phase16_artifact_manifest.json
- scripts/smoke_trace_reproducibility.py
- tests/test_trace_reproducibility.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_trace_reproducibility.py -q initially failed because financial_evidence_engine.traceability did not exist.
- After implementation, tests/test_trace_reproducibility.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest: 82 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check printed runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=20 sample_memo_verdict=support markdown_lines=137
```

Known limitations:

```text
Phase 16 traces the three portfolio case studies, not every one of the 60 benchmark tasks.
The trace store is a local SQLite artifact, not a production observability backend.
Trace records point to current artifact paths; broader report regeneration belongs to Phase 17.
```

### Phase 17: Polished Report PDF / Portfolio Artifact

Commit:

```text
feat: build portfolio-ready technical report
```

What changed:

```text
Added a one-command portfolio report builder for recruiter-facing artifacts.

Added:
- PortfolioReportPackage, PortfolioReportSection, FigureSpec, TableSpec, and PortfolioReportArtifactManifest
- scripts/build_portfolio_report.py
- reports/final_report.pdf
- reports/final_report.md
- reports/figures/method_comparison.json
- reports/figures/failure_mode_breakdown.json
- reports/figures/validator_coverage.json
- reports/figures/case_study_flow.json
- reports/figures/chart_evidence_reconciliation.json
- reports/tables/case_study_summary.json
- reports/tables/deck_reconciliation.json
- reports/tables/reproducibility_commands.json
- reports/portfolio_report_manifest.json
- reports/resume_bullet.txt
- tests/test_portfolio_report.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_portfolio_report.py -q initially failed because financial_evidence_engine.reports.portfolio_report and the report command registration did not exist.
- After implementation, tests/test_portfolio_report.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest: 85 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check printed runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase17 portfolio report build check printed sections=10 pages=10 case_studies=3 figures=5 tables=3 pdf=reports/final_report.pdf markdown=reports/final_report.md manifest=reports/portfolio_report_manifest.json
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=21 sample_memo_verdict=support markdown_lines=138
```

Known limitations:

```text
The PDF writer is a lightweight stdlib text renderer, not a designed slide deck or typeset publication system.
Figures and tables are portable JSON specs, not rendered chart images.
The report is generated from deterministic local artifacts; broader live-document report regeneration remains deferred.
```

### Phase 18: Lightweight Demo UI

Commit:

```text
feat: add lightweight due diligence demo UI
```

What changed:

```text
Added a local Streamlit demo over existing checked-in artifacts.

Added:
- app.py Streamlit entry point
- DemoState, CaseStudyReplay, and DemoClaimResult
- load_demo_state() for local artifact-backed demo state
- replay_case_study() for the three portfolio case studies
- run_local_claim_demo() for one local deterministic claim verification path
- render_demo_markdown() fallback when Streamlit is not available
- scripts/smoke_demo_ui.py
- scripts/smoke_streamlit_start.py
- tests/test_demo_ui.py
- pyproject demo optional dependency group
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_demo_ui.py -q initially failed because financial_evidence_engine.demo did not exist.
- After implementation, tests/test_demo_ui.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts app.py
- python3 -m pytest: 89 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check printed runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase17 portfolio report build check printed sections=10 pages=10 case_studies=3 figures=5 tables=3 pdf=reports/final_report.pdf markdown=reports/final_report.md manifest=reports/portfolio_report_manifest.json
- phase18 demo UI smoke check printed pages=4 case_studies=3 methods=5 local_claim_verdict=support api_key_required=False app=app.py
- phase18 Streamlit start smoke check printed streamlit_started=True url=http://127.0.0.1:54900 app=app.py
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=23 sample_memo_verdict=support markdown_lines=140
```

Known limitations:

```text
The UI is a local Streamlit demo, not a production web application.
Only the local AAPL revenue claim path is wired for new ad hoc input.
Case study replay is artifact-backed; it does not rerun every retrieval method live from the UI.
```

### Phase 19: Productionization Slice

Commit:

```text
feat: harden local production workflow
```

What changed:

```text
Added a production-oriented local CLI and artifact hygiene helpers.

Added:
- financial_evidence_engine.cli
- financial_evidence_engine.production
- financial-evidence console entry point
- CLI commands: verify-claim, build-corpus, run-eval, build-case-studies, build-report, serve-demo
- CONFIG_PROFILES for local and CI, both offline
- ERROR_TAXONOMY and ProductionError
- ArtifactVersion, CacheInvalidationPlan, and ProvenanceCheck
- structured_log()
- scripts/smoke_cli_workflow.py
- tests/test_cli_workflow.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_cli_workflow.py -q initially failed because financial_evidence_engine.cli, financial_evidence_engine.production, and scripts/smoke_cli_workflow.py did not exist.
- After implementation, tests/test_cli_workflow.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts app.py
- python3 -m pytest: 94 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check printed runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase17 portfolio report build check printed sections=10 pages=10 case_studies=3 figures=5 tables=3 pdf=reports/final_report.pdf markdown=reports/final_report.md manifest=reports/portfolio_report_manifest.json
- phase18 demo UI smoke check printed pages=4 case_studies=3 methods=5 local_claim_verdict=support api_key_required=False app=app.py
- phase18 Streamlit start smoke check printed streamlit_started=True url=http://127.0.0.1:55775 app=app.py
- phase19 CLI workflow smoke check printed commands=6 verify_verdict=support raw_chunks=482 eval_tasks=60 case_studies=3 report_pages=10 serve_demo=True network_enabled=False
- missing PDF CLI check returned code 2 and JSON error_code=missing_pdf without traceback
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=24 sample_memo_verdict=support markdown_lines=141
```

Known limitations:

```text
The CLI is local-first and does not expose a persistent service API.
serve-demo supports dry-run checks and can launch Streamlit, but this phase does not add process supervision.
FastAPI remains intentionally deferred.
```

### Phase 20: Final Resume / Interview Packaging

Commit:

```text
docs: package final interview and resume story
```

What changed:

```text
Added final application and interview packaging.

Added:
- docs/interview_story.md
- docs/resume_bullets.md
- docs/system_design_notes.md
- docs/failure_modes.md
- docs/demo_script.md
- README 2-minute read, 10-minute artifact, and 30-minute reproduction entry points
- scripts/smoke_interview_packaging.py
- tests/test_interview_packaging.py
```

Validation:

```text
Red-green TDD:
- python3 -m pytest tests/test_interview_packaging.py -q initially failed because the docs, README entry points, and smoke script did not exist.
- After implementation, tests/test_interview_packaging.py passed.

Final checks:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts app.py
- python3 -m pytest: 97 passed
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check printed companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check printed sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check printed company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check printed nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check printed verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check printed tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check printed tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- real retrieval evaluation smoke check printed tasks=60 corpus_mode=benchmark corpus_documents=320 raw_chunks=0 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=346
- phase9 case studies smoke check printed case_studies=3 methods=5 json_artifacts=3 markdown_artifacts=3 summary=reports/case_studies/index.md
- phase10 deck chart extraction smoke check printed deck_pages=1 chart_evidence=1 chart_tasks=1 reconciliation_rows=1 verdict=support
- phase11 raw corpus smoke check printed raw_chunks=482 curated_documents=320 companies=10 sec_paragraph_companies=10 transcript_chunks=30 deck_pages=1 corpus_modes=benchmark,raw
- raw corpus retrieval smoke check printed tasks=60 corpus_mode=raw corpus_documents=482 raw_chunks=482 methods=5 bm25_numeric_correctness=0 full_verdict_accuracy=0.8333333333333333333333333333 failure_cases=617
- phase12 embedding backend smoke check printed methods=bm25,dense_proxy,hybrid_proxy,graph,full_engine skipped=dense_real,hybrid_real provider=deterministic-token-v1 cached_vectors=320 manifest=embedding_manifest.json optional_available=False
- phase13 LLM decomposition smoke check printed complex_claims=5 providers=rule_based,recorded_llm rule_based_subclaims=7 llm_subclaims=19 rejected=0 json_artifact=experiments/llm_decomposition/phase13_decomposition_comparison.json markdown_artifact=reports/llm_decomposition/phase13_decomposition_comparison.md live_available=False
- phase14 narrative/causal smoke check printed narrative_tasks=10 claim_types=6 partial_verdicts=5 overclaim_cases=8 overclaim_rate=0.8 unsupported_causal=5 json_artifact=experiments/narrative_causal/phase14_narrative_causal_report.json markdown_artifact=reports/narrative_causal/phase14_narrative_causal_report.md
- phase15 adversarial smoke check printed adversarial_tasks=120 failure_modes=12 taxonomy_entries=12 validators=11 full_engine_accuracy=0.75 explainable_failure_rate=1 perfect_accuracy_required=False json_artifact=experiments/adversarial/phase15_adversarial_report.json markdown_artifact=reports/adversarial/phase15_adversarial_report.md
- phase16 trace smoke check printed runs=3 retrieval_traces=3 verification_traces=3 evidence_traces=3 memo_traces=3 artifact_records=3 trace_integrity=True case_studies_regenerated=3 db=experiments/traces/phase16_trace.sqlite manifest=reports/traces/phase16_artifact_manifest.json
- phase17 portfolio report build check printed sections=10 pages=10 case_studies=3 figures=5 tables=3 pdf=reports/final_report.pdf markdown=reports/final_report.md manifest=reports/portfolio_report_manifest.json
- phase18 demo UI smoke check printed pages=4 case_studies=3 methods=5 local_claim_verdict=support api_key_required=False app=app.py
- phase18 Streamlit start smoke check printed streamlit_started=True url=http://127.0.0.1:58595 app=app.py
- phase19 CLI workflow smoke check printed commands=6 verify_verdict=support raw_chunks=482 eval_tasks=60 case_studies=3 report_pages=10 serve_demo=True network_enabled=False
- phase20 interview packaging smoke check printed docs=5 readme_2min=True report_10min=True repo_30min=True evidence_framing=True
- phase8 memo smoke check printed verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0
- final report package smoke check printed tasks=60 charts=4 tables=3 commands=25 sample_memo_verdict=support markdown_lines=142
```

Known limitations:

```text
Final packaging is optimized for applications and interviews, not a production deployment.
The strongest demo remains the local deterministic evidence engine; live data ingestion and broad chart parsing remain out of scope.
Future changes should be driven by recruiter/interviewer feedback or a new roadmap.
```

## Current State

Project root:

```text
.
```

Phase 0 planning and repository skeleton are complete.

The repository now includes:

```text
AGENTS.md
README.md
ROADMAP.md
RUNBOOK.md
TASK_MEMORY.md
VALIDATION.md
pyproject.toml
configs/
src/financial_evidence_engine/
tests/
```

Implementation currently covers configuration loading, ticker/CIK lookup, SEC/XBRL source metadata registry, source payload caching, version hashes, local extraction into evidence units, financial normalization guardrails, local evidence graph construction, deterministic claim verification, a 60-task due-diligence gold specification, a deterministic evaluation/ablation harness, real local retrieval baselines over a 320-document benchmark corpus, portfolio case studies, minimal investor-deck chart extraction, raw financial document corpus indexing, pluggable embedding/reranking interfaces, validator-gated recorded LLM decomposition, narrative/causal partial-verdict verification, adversarial/red-team evaluation, evidence trace persistence, auditable memo generation, final report packaging, a portfolio-ready PDF/Markdown report artifact, a lightweight local Streamlit demo UI, a local production CLI workflow, and final interview packaging. Broad chart extraction and live LLM decomposition remain out of scope for the completed portfolio roadmap.

## Project Identity

**Name:** Multimodal Financial Due-Diligence Evidence Engine

**Role in portfolio:** Claim-level financial evidence verification system for due-diligence workflows.

**Core question:**

```text
Can AI synthesize and verify financial evidence across messy multimodal documents without hallucinating?
```

**Main story:**

```text
This is not a chatbot and not a PDF QA app.
It is a claim-level evidence verification engine for financial due diligence.
```

## Principal Objective

Build a system that takes financial claims and produces auditable verification:

```text
input: financial claim or due-diligence question
output:
  - decomposed subclaims
  - supporting evidence
  - contradicting evidence
  - numeric reconciliation
  - citation validation
  - fiscal-period validation
  - final verdict: support / contradict / insufficient
  - due-diligence memo
```

## Scope Boundary

Keep this project focused on financial evidence reasoning.

### In Scope

```text
SEC EDGAR metadata and filings
SEC XBRL company facts
FMP financial data and transcripts
investor decks / earnings presentation PDFs
text extraction
table extraction
XBRL extraction
transcript parsing
chart extraction, if time allows
financial normalization
evidence graph
claim verification
numeric validators
citation validators
fiscal-period validators
contradiction detection
due-diligence memo generation
RAG / GraphRAG / full-system comparison
```

### Out of Scope

```text
general-purpose agent infrastructure
agent tool registry as main product
sandboxed execution as main product
trace replay dashboard as main product
coding benchmark tasks
data analysis benchmark tasks
optimization benchmark tasks
```

Those belong to A2: Sandboxed Tool-Use Agent Evaluation Harness.

## Key Design Decisions

1. **Project name changed from benchmark to engine.**

   Old framing:

   ```text
   Finance Evidence Retrieval & Citation Reliability Benchmark
   ```

   New framing:

   ```text
   Multimodal Financial Due-Diligence Evidence Engine
   ```

2. **The output is a due-diligence memo, not a chat response.**

3. **The unit of reasoning is a claim, not a user question.**

4. **Every numeric statement must be validator-checkable.**

5. **Every citation must map to source document, section/page, and evidence span.**

6. **The system must be able to say insufficient evidence.**

7. **GraphRAG is useful but not sufficient.**

   The intended formula is:

   ```text
   GraphRAG + multimodal extraction + financial validators + claim-level citation
   ```

## MVP Definition

Recommended MVP:

```text
5-10 large-cap companies
3 fiscal years
10-K / selected 10-Q / transcripts / investor decks
50-100 high-quality tasks
```

Initial task families:

```text
revenue growth
margin trend
cash flow quality
leverage
risk factor changes
management guidance vs actuals
deck narrative vs filing evidence
```

## Original MVP checklist

This historical checklist records the original build order. It is no longer the active roadmap; Phase 9 through Phase 20 are complete. Items that remain intentionally outside the public portfolio scope are listed below as out-of-scope rather than unchecked work.

### Step 1: Planning and Skeleton

```text
[x] Create README.md
[x] Create AGENTS.md
[x] Create VALIDATION.md
[x] Create RUNBOOK.md
[x] Create pyproject.toml
[x] Create configs/
[x] Create src/ package layout
[x] Create tests/ layout
[x] Select initial company universe
```

### Step 2: Data Layer

```text
[x] Implement SEC client
[x] Implement document registry
[x] Implement cache/version hash
[x] Store filing metadata
[x] Store local FMP transcript payloads and metadata sidecars
[x] Store investor-deck fixture metadata for the Phase 10 chart evidence slice
```

### Step 3: Extraction Layer

```text
[x] Extract filing text
[x] Split filing sections
[x] Parse XBRL facts
[x] Parse transcripts
[x] Extract tables
[x] Add text-extractable deck PDF parsing for the Phase 10 fixture
[x] Add narrow investor-deck chart evidence extraction for one reproducible case
```

### Known out-of-scope items

```text
- reusable live FMP client as a required runtime path
- broad investor-deck registry
- general visual chart understanding, OCR, axis detection, or plot digitization
- full SEC archive indexing
- trained neural retrieval model
- live LLM decomposition as a default dependency
```

### Step 4: Normalization Layer

```text
[x] Entity linker
[x] Ticker/CIK resolver
[x] Fiscal period resolver
[x] Metric alias mapper
[x] Unit normalizer
[x] Currency normalizer
[x] Annual vs quarterly guardrails
```

### Step 5: Evidence Graph

```text
[x] Define graph nodes
[x] Define graph edges
[x] Build graph from documents and evidence units
[x] Link claims to evidence units
[x] Link metrics across documents
[x] Track risk themes across years
```

### Step 6: Claim Verification

```text
[x] Claim decomposer
[x] Evidence selector
[x] Numeric reconciler
[x] Citation validator
[x] Fiscal-period validator
[x] Contradiction detector
[x] Verdict generator
```

### Step 7: Evaluation

```text
[x] Build 50-100 task gold set
[x] Implement metrics
[x] Implement BM25 baseline
[x] Implement dense/hybrid baseline
[x] Implement GraphRAG baseline
[x] Implement full-system run
[x] Run ablations
```

### Step 8: Final Report

```text
[x] Generate due-diligence memo example
[x] Create charts
[x] Write final report
[x] Add reproducibility instructions
[x] Polish resume bullet
```

## Acceptance Criteria

The project is portfolio-ready when:

```text
one claim links to multiple evidence units
numbers are reconciled against structured financial facts
citations are checked for support
fiscal periods are validated
unsupported claims are explicitly flagged
contradictions across sources can be shown
ordinary RAG baseline fails in measurable ways
full evidence engine improves citation/numeric/unsupported-claim metrics
one polished due-diligence memo is included
```

## Failure Modes to Watch

```text
scope creep into generic agent infra
too many companies before extraction works
too much UI before validators work
overusing GraphRAG without financial normalization
treating citations as decoration instead of validated evidence
mixing fiscal year, calendar year, and filing date
mixing annual and quarterly values
using charts before table/text extraction is stable
```

## Suggested First Companies

Pick companies with rich disclosures and public decks:

```text
AAPL
MSFT
NVDA
AMZN
GOOGL
META
JPM
WMT
TSLA
NFLX
```

Do not start with all ten if time is limited. Start with 3 companies, then expand.

## Resume Target

Final bullet should communicate:

```text
multimodal financial documents
claim-level evidence verification
BM25, dense-proxy, hybrid, graph, and validator-augmented retrieval
numeric reconciliation
citation validation
fiscal-period checks
contradiction detection
due-diligence memo
```

Preferred bullet:

> Built a multimodal financial due-diligence evidence engine for claim-level verification over SEC/XBRL filings, earnings transcripts, and investor-deck evidence; benchmarked BM25, dense-proxy, hybrid, graph, and validator-augmented retrieval on 60 due-diligence tasks and 120 adversarial cases, generating auditable memos with numeric reconciliation, citation validation, fiscal-period checks, contradiction detection, and reproducible evidence traces.
