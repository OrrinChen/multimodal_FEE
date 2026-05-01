# Task Memory: Multimodal Financial Due-Diligence Evidence Engine

## Latest Status

Current branch:

```text
codex/ashare-radar-phase1a
```

Latest commit:

```text
feat: add auditable due diligence memo
```

Current phase:

```text
Final report and reproducibility package
```

Main blocker:

```text
Final report packaging, charts/tables, reproducibility guide, and polished resume bullet are not complete yet.
```

Next recommended action:

```text
Package the final report with evaluation charts/tables, a sample due-diligence memo artifact, reproducibility instructions, and the final resume bullet.
```

Latest workflow update:

```text
Completed Phase 8 auditable due-diligence memo.

Added:
- DueDiligenceMemo, MemoClaim, MemoConclusion, EvidenceTableRow, NumericReconciliationRow, and MemoIssue models
- memo builder from ClaimVerificationResult outputs
- required memo sections: executive summary, key claims, evidence table, numeric reconciliation, contradictions, risk flags, unresolved claims, and limitations
- conclusion traces with citation, source document, page/section, metric, period, and validator results
- markdown serialization that separates evidence summaries from inference
- Phase 8 smoke script and test coverage
```

Latest validation:

```text
Passed:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src scripts
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']
- phase1 registry smoke check: companies=3 documents=6 aligned_periods=3
- phase2 extraction smoke check: sections=4 xbrl=1 transcripts=1 tables=1
- phase3 normalization smoke check: company=AAPL period=FY2024 metric=revenue left_amount=391035000000.000 right_amount=391035000000 comparable=True
- phase4 evidence graph smoke check: nodes=8 edges=14 claim_evidence=2 metric_evidence=2
- phase5 claim verification smoke check: verdict=support subclaims=1 evidence=1 checks=5
- phase6 task set smoke check: tasks=60 families=6 verdicts=3
- phase7 evaluation smoke check: tasks=60 baselines=6 ablations=6 full_verdict_accuracy=1 validators_matter=True naive_rag_fails=True
- phase8 memo smoke check: verdict=support sections=8 evidence_rows=1 numeric_rows=1 unsupported=0

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

## Current State

Project folder created as:

```text
/Users/orynwilder/Documents/New project 2/multimodal-financial-evidence-engine
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

Implementation currently covers configuration loading, ticker/CIK lookup, SEC/XBRL source metadata registry, source payload caching, version hashes, local extraction into evidence units, financial normalization guardrails, local evidence graph construction, deterministic claim verification, a 60-task due-diligence gold specification, a deterministic evaluation/ablation harness, and auditable memo generation. Production semantic retrieval, final report packaging, and LLM-assisted decomposition are not implemented yet.

## Project Identity

**Name:** Multimodal Financial Due-Diligence Evidence Engine

**Role in portfolio:** S-level AI for finance project. Business-shock project.

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

## Implementation Order

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
[ ] Implement FMP client module (local snapshot captured; reusable code path still deferred)
[x] Implement document registry
[x] Implement cache/version hash
[x] Store filing metadata
[x] Store local FMP transcript payloads and metadata sidecars
[ ] Store investor deck metadata
```

### Step 3: Extraction Layer

```text
[x] Extract filing text
[x] Split filing sections
[x] Parse XBRL facts
[x] Parse transcripts
[x] Extract tables
[ ] Add deck PDF parsing
[ ] Add chart extraction only after table/text pipeline works
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
[ ] Create charts
[ ] Write final report
[ ] Add reproducibility instructions
[ ] Polish resume bullet
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
GraphRAG
numeric reconciliation
citation validation
fiscal-period checks
contradiction detection
due-diligence memo
```

Preferred bullet:

> Built a multimodal financial due-diligence evidence engine combining SEC/FMP data, earnings transcripts, investor decks, GraphRAG, table/chart extraction, and claim-level validators to reconcile financial narratives, detect unsupported claims, numeric mismatches, fiscal-period errors, and cross-document contradictions.
