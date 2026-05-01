# Multimodal Financial Due-Diligence Evidence Engine Roadmap

## 0. Current State and Automation Workflow

Completed:

- [x] Initial project positioning documented
- [x] `ROADMAP.md` created
- [x] `TASK_MEMORY.md` created
- [x] Codex automation workflow files added:
  - `AGENTS.md`
  - `README.md`
  - `VALIDATION.md`
  - `RUNBOOK.md`
- [x] Python project metadata created in `pyproject.toml`
- [x] `configs/` created with first 3-company universe
- [x] `src/financial_evidence_engine/` package layout created
- [x] `tests/` layout created with Phase 0 skeleton tests
- [x] Phase 1 SEC/XBRL document registry implemented:
  - ticker <-> CIK lookup
  - SEC submissions and XBRL company facts client endpoints
  - document metadata schema
  - source payload cache and version hashes
  - filing date, publication date, and fiscal period kept separate
- [x] Phase 2 extraction implemented:
  - SEC filing text section splitting
  - XBRL fact extraction into traceable evidence units
  - transcript speaker/section parsing
  - markdown table numeric extraction
  - `EvidenceUnit` schema with source spans
- [x] Phase 3 financial normalization implemented:
  - entity / ticker / CIK resolver
  - fiscal and calendar period resolver
  - period end date handling from document metadata
  - metric alias mapper
  - currency and unit scale normalizers
  - comparison guardrails for company, period, metric, currency, and scale
- [x] Phase 4 evidence graph implemented:
  - typed graph nodes and edges
  - graph builder from document metadata and evidence units
  - claim-to-evidence links
  - metric-to-evidence links across source documents
  - risk-theme links across fiscal years
- [x] Phase 5 claim verification implemented:
  - claim and subclaim models
  - graph-based evidence selector
  - citation, fiscal-period, source-consistency, numeric, and unsupported-claim validators
  - support / contradict / insufficient verdict generation
  - validator-readable result serialization
- [x] Phase 6 multimodal due-diligence task set implemented:
  - 60 seed tasks across 10 large-cap companies
  - six due-diligence task families
  - expected evidence units, numeric checks, source-type constraints, verdicts, and known distractors
  - task-set smoke check and Phase 6 tests
- [x] Phase 7 evaluation and ablations implemented:
  - deterministic metrics over Phase 6 task specs
  - six diagnostic baseline profiles
  - six ablation profiles
  - acceptance findings for validators, graph retrieval, naive RAG failure, and full-system gains
- [x] Phase 8 auditable due-diligence memo implemented:
  - executive summary and key claims
  - evidence table and numeric reconciliation
  - contradiction, risk flag, unsupported-claim, and limitations sections
  - traceable conclusions with citations, source documents, periods, metrics, and validator results

Current phase:

- Final report and reproducibility package

Urgent short-term data action:

- [x] Captured a local FMP snapshot before Ultimate access expires.
- Snapshot location:
  - `data/cache/fmp/`
- Snapshot scope:
  - 10 symbols: AAPL, MSFT, NVDA, AMZN, GOOGL, META, JPM, WMT, TSLA, NFLX
  - annual and quarterly financial statements
  - annual and quarterly as-reported statements
  - key metrics, ratios, enterprise values, growth metrics, and financial scores
  - transcripts and transcript dates for 2022-2025
  - analyst estimates and price targets
  - earnings calendar
  - historical daily prices and market capitalization from 2022-01-01 to 2026-04-30
  - dividends, splits, shares float, peers, executives, employee counts, ratings, news, and segment revenue
- Store raw payloads locally with `source`, `endpoint`, `symbol`, `period`, `retrieved_at`, and `version_hash`.
- Do not make real-time quote access a core dependency. Historical market context is enough for this due-diligence evidence engine.

Next recommended action:

- Package the final report:
  - add charts/tables from the deterministic evaluation harness
  - include a sample due-diligence memo artifact
  - write reproducibility instructions and final resume bullet

Near-term vertical slice:

```text
10 companies
3 fiscal years
60 claim-verification task specs
SEC filings + XBRL facts first
validated numeric/fiscal/citation outputs before GraphRAG or chart extraction
```

Deferred:

- cloud deployment
- production integration
- full 5-10 company corpus
- investor deck registry until SEC/XBRL extraction is stable
- PDF binary extraction beyond simple HTML/text fixtures
- chart extraction
- real-time market data dependency
- UI
- broad GraphRAG experimentation before validators work

External data policy:

```text
SEC/XBRL = authoritative filing truth
FMP = secondary structured source + transcripts + estimates + historical market context
real-time quotes = optional only, not required for MVP
```

FMP usage rules:

```text
do not commit FMP_API_KEY
do not commit raw paid FMP payloads
cache local FMP snapshots with retrieved_at and version_hash
label every FMP-derived evidence unit as secondary source
never mix FMP normalized values with SEC raw facts without source labels
use SEC/XBRL as numeric validator authority when conflicts appear
```

## 1. 项目定位

**项目名:** Multimodal Financial Due-Diligence Evidence Engine

**一句话:**

> Can AI synthesize financial evidence across messy multimodal documents without hallucinating?

**中文定位:**

这个项目不是 PDF QA app，也不是普通金融 RAG。它是一个面向投行、PE、信用分析、公募研究的多模态金融尽调证据引擎，目标是把 SEC filings、XBRL facts、earnings transcripts、investor decks、表格、图表和财务指标转成可验证的 claim-level evidence graph。

核心链路:

```text
financial claim
-> decompose subclaims
-> retrieve evidence
-> extract table/chart/text/XBRL support
-> normalize company / metric / period / unit
-> reconcile numbers
-> build evidence graph
-> detect unsupported or contradictory claims
-> produce auditable due-diligence memo
```

## 2. 核心卖点

传统金融 RAG 容易错在:

```text
wrong evidence
wrong citation
wrong number
wrong fiscal period
wrong unit
wrong company/entity
unsupported conclusion
missed contradiction
```

本项目的差异化:

```text
GraphRAG
+ multimodal extraction
+ financial normalization
+ numeric reconciliation
+ fiscal-period validation
+ claim-level citation validation
+ contradiction detection
```

目标不是让模型说得像 analyst，而是让系统能回答:

```text
这个金融判断被哪些证据支持？
哪些证据反驳它？
数字是否能复算？
引用是否精确？
期间和单位是否对齐？
证据不足时能不能明确说 insufficient evidence？
```

## 3. 明确边界

### 本项目要做

```text
SEC / FMP / IR document ingestion
document registry and source provenance
10-K / 10-Q / 8-K text extraction
XBRL fact extraction
earnings transcript parsing
investor deck PDF parsing
table extraction
chart extraction, if MVP time allows
financial metric normalization
fiscal period resolution
evidence graph construction
claim decomposition
claim-level evidence retrieval
numeric reconciliation
citation validation
source consistency validation
contradiction detection
auditable due-diligence memo generation
baseline comparison and ablations
```

### 本项目不做

```text
general-purpose agent framework
tool-use agent architecture benchmark
sandbox execution as main product
trace replay dashboard as main product
coding / data / optimization agent task suites
leaderboard-style agent evaluation
```

这些属于 A2: Sandboxed Tool-Use Agent Evaluation Harness。

## 4. MVP 范围

为避免项目失控，MVP 收窄到:

```text
companies: 5-10 large-cap companies
period: 3 fiscal years
documents per company:
  - 10-K
  - selected 10-Q
  - earnings transcripts
  - investor decks / earnings presentations

initial task families:
  - revenue growth
  - margin trend
  - cash flow quality
  - debt / leverage
  - risk factor changes
  - management guidance vs actuals
  - deck narrative vs SEC filing evidence
```

MVP 成功标准:

```text
50-100 high-quality claim verification tasks
each task requires multi-document evidence
each answer includes citations
each numeric claim is validator-checkable
system can output support / contradict / insufficient
```

## 5. 数据源设计

### Structured ground truth

```text
SEC EDGAR company submissions
SEC XBRL company facts
FMP financial statements as secondary source
FMP as-reported statements as cross-check source
FMP analyst estimates and price targets
FMP earnings calendar
FMP historical prices around event windows
```

用途:

```text
authoritative filing metadata
financial metric ground truth
period and publication date alignment
validator reference values
secondary-source cross-checks
market reaction context around filings and earnings calls
```

### FMP snapshot corpus

Captured local corpus:

```text
data/cache/fmp/
  transcripts/
  financial_statements/
  as_reported/
  key_metrics/
  ratios/
  enterprise_values/
  growth/
  financial_scores/
  analyst_estimates/
  price_targets/
  earnings_calendar/
  historical_prices/
  market_context/
  corporate_actions/
  ratings/
  segment_revenue/
  news/
```

Snapshot status:

```text
retrieved_at window: 2026-04-30T14:11:15Z to 2026-04-30T15:15:35Z
symbols: AAPL, MSFT, NVDA, AMZN, GOOGL, META, JPM, WMT, TSLA, NFLX
manifest_records: 700
payload_json_files: 700
metadata_files: 700
remaining_failures: 0
real-time quotes: not downloaded
raw paid payloads: ignored by git under data/cache/
```

Snapshot metadata:

```text
source: FMP
endpoint
symbol
fiscal_year
fiscal_quarter
period
retrieved_at
version_hash
raw_payload_path
```

Realtime policy:

```text
not required for MVP
not used as evidence truth
only useful for live dashboards or immediate market-reaction analysis
prefer historical daily/intraday event windows over real-time quotes
```

### Text corpus

```text
10-K / 10-Q / 8-K
MD&A
risk factors
earnings call transcripts
press releases
management commentary
```

用途:

```text
management explanation
risk disclosures
strategy claims
cross-document narrative comparison
```

### Multimodal corpus

```text
investor presentations
earnings decks
tables inside filings
segment charts
margin bridge charts
cash-flow bridge charts
```

用途:

```text
deck claim verification
chart/table number reconciliation
presentation narrative vs filing contradiction detection
```

## 6. Target Repo Structure

```text
multimodal-financial-evidence-engine/
  README.md
  ROADMAP.md
  TASK_MEMORY.md
  pyproject.toml

  configs/
    companies.yaml
    document_sources.yaml
    extraction.yaml
    retrieval.yaml
    graph.yaml
    validators.yaml
    evaluation.yaml

  src/
    data/
      sec_client.py
      fmp_client.py
      ir_pdf_downloader.py
      document_registry.py
      cache.py

    extraction/
      text_extractor.py
      table_extractor.py
      chart_extractor.py
      xbrl_extractor.py
      transcript_parser.py
      slide_parser.py

    normalization/
      entity_linking.py
      fiscal_period_resolver.py
      metric_mapper.py
      unit_normalizer.py
      currency_normalizer.py

    evidence_graph/
      nodes.py
      edges.py
      graph_builder.py
      community_summary.py
      claim_graph.py

    retrieval/
      bm25.py
      dense_retriever.py
      hybrid_retriever.py
      reranker.py
      graph_retriever.py

    reasoning/
      claim_decomposer.py
      evidence_selector.py
      numeric_reconciler.py
      contradiction_detector.py
      memo_writer.py

    validators/
      citation_validator.py
      numeric_validator.py
      fiscal_period_validator.py
      source_consistency_validator.py
      unsupported_claim_detector.py

    evaluation/
      task_set.py
      gold_builder.py
      metrics.py
      failure_taxonomy.py
      ablations.py

    reports/
      plots.py
      tables.py
      report_builder.py

  notebooks/
    01_document_ingestion.ipynb
    02_extraction_and_normalization.ipynb
    03_evidence_graph.ipynb
    04_claim_verification.ipynb
    05_multimodal_financial_tasks.ipynb
    06_final_report.ipynb

  tests/
    test_fiscal_period_resolution.py
    test_numeric_reconciliation.py
    test_citation_validator.py
    test_claim_graph.py
```

## 7. Phases

### Phase 1: Document Registry and Ingestion

Goal: 建立可追踪的数据层。

Build:

```text
company universe
ticker <-> CIK mapping
SEC filing metadata ingestion
FMP snapshot ingestion from local cached payloads
investor deck metadata registry
document download and cache
publication date tracking
fiscal period mapping
source version hash
```

Document schema:

```text
document_id
company
ticker
cik
source_type
filing_type
fiscal_year
fiscal_quarter
period_end_date
publication_date
source_url or accession_number
retrieved_at
version_hash
source_authority: authoritative / secondary / market_context
```

Acceptance criteria:

```text
every evidence unit can trace back to source document
every document has fiscal period and publication date
same company documents can be aligned across source types
filing date and fiscal period are not confused
FMP documents are marked secondary and aligned to SEC/XBRL periods before use
```

### Phase 1.5: FMP Snapshot Capture

Goal: 在 FMP Ultimate 到期前保存可复现的二级数据源快照。

Build:

```text
FMP client using FMP_API_KEY env var
snapshot downloader for selected symbols and years
raw payload cache under data/cache/fmp/
metadata sidecars with endpoint, symbol, period, retrieved_at, version_hash
transcript payload registry
financial statement payload registry
as-reported payload registry
analyst estimate / price target registry
earnings calendar registry
historical price event-window registry
```

Do not build:

```text
real-time quote dependency
trading dashboard
live market monitor
committed paid raw payloads
```

Acceptance criteria:

```text
FMP_API_KEY is read only from environment
raw FMP payloads are cached locally and ignored by git
each cached payload has retrieved_at and version_hash
FMP transcripts can feed the transcript parser
FMP financial statements can be compared against SEC/XBRL but are labeled secondary
historical prices are tied to filing/transcript event dates, not live quote state
```

### Phase 2: Text / Table / XBRL / Transcript Extraction

Goal: 把不同模态统一成 evidence units。

Build:

```text
PDF text extraction
10-K / 10-Q section splitter
XBRL fact extractor
earnings transcript parser
table extractor
slide parser
chart extraction if time allows
```

Evidence unit schema:

```text
evidence_id
document_id
company
fiscal_period
modality: text/table/chart/xbrl/transcript
page_or_section
raw_text
normalized_metric
numeric_value
unit
currency
source_span
```

Acceptance criteria:

```text
10-K text can be chunked by section
XBRL facts map to standard metrics
transcripts split by speaker / section
tables produce normalized numeric evidence
```

### Phase 3: Financial Normalization Layer

Goal: 解决金融数据最常见的错位问题。

Build:

```text
[x] entity linking
[x] ticker <-> CIK resolver
[x] fiscal year / fiscal quarter resolver
[x] period end date resolver
[x] metric alias mapper
[x] unit normalizer
[x] currency normalizer
[x] annual vs quarterly guardrails
```

Must handle:

```text
revenue / net sales / total net sales
operating income / EBIT
net income / earnings
dollars / thousands / millions / billions
FY2023 vs CY2023
quarterly vs annual values
```

Acceptance criteria:

```text
[x] does not mix FY2023 and CY2023
[x] does not mix quarterly and annual revenue
[x] does not mix $ millions and $ thousands
[x] does not compare different companies by accident
```

### Phase 4: Evidence Graph

Goal: 从 top-k retrieval 升级到可推理证据图。

Graph nodes:

```text
[x] Company
[x] Document
[x] FiscalPeriod
[x] Metric
[x] Claim
[x] EvidenceUnit
[x] RiskFactor
[x] Segment
[x] Person/Speaker
[x] Event
```

Graph edges:

```text
[x] reported_in
[x] supports
[x] contradicts
[x] mentions
[x] same_metric_as
[x] same_period_as
[x] changed_from
[x] guidance_for
[x] risk_related_to
```

Acceptance criteria:

```text
[x] one claim links to multiple evidence units
[x] one metric links to corresponding evidence across filings/decks/transcripts
[x] risk theme wording can be tracked across years
[x] cross-document evidence can be aggregated
```

### Phase 5: Claim Decomposition and Verification

Goal: 验证金融 claim，而不是直接生成答案。

Example input:

```text
Company A's margin expansion was driven by operating leverage rather than one-time cost cuts.
```

Expected decomposition:

```text
subclaim_1: margin expanded over period X
subclaim_2: revenue grew faster than operating expenses
subclaim_3: management attributed this to operating leverage
subclaim_4: no major one-time cost cut explains the change
```

Each subclaim needs:

```text
[x] required evidence type
[x] retrieved evidence
[x] numeric check
[x] citation
[x] support / contradict / insufficient
[x] confidence
```

Acceptance criteria:

```text
[x] system can say insufficient evidence
[x] system can mark contradiction
[x] system does not invent evidence
[x] system produces validator-readable outputs
```

### Phase 6: Multimodal Due-Diligence Task Set

Goal: 构建自己的高质量 benchmark。

Task families:

```text
[x] single-company trend
[x] cross-company comparison
[x] management claim verification
[x] risk contradiction
[x] guidance vs actuals
[x] chart/table reconciliation
```

Gold labels:

```text
[x] expected evidence units
[x] expected numeric checks
[x] allowed source types
[x] expected verdict
[x] known distractors
```

Acceptance criteria:

```text
[x] 50-100 tasks
[x] each task is multi-hop or multi-document
[x] each answer requires citation
[x] each numeric claim can be validator checked
```

### Phase 7: Evaluation and Ablations

Baselines:

```text
[x] BM25 RAG
[x] dense RAG
[x] hybrid retrieval + reranker
[x] GraphRAG only
[x] multimodal extraction only
[x] full evidence engine
```

Metrics:

```text
[x] evidence recall@k
[x] citation exactness
[x] numeric correctness
[x] fiscal-period correctness
[x] entity correctness
[x] unsupported-claim rate
[x] contradiction detection accuracy
[x] answer faithfulness
[x] memo usefulness
[x] latency
[x] cost
```

Ablations:

```text
[x] without graph
[x] without numeric validator
[x] without fiscal-period validator
[x] without chart/table extraction
[x] without contradiction detector
[x] without reranker
```

Acceptance criteria:

```text
[x] results show why validators matter
[x] results show why graph retrieval matters
[x] results show where naive RAG fails
[x] full system improvement is not just prompt engineering
```

### Phase 8: Auditable Due-Diligence Memo

Goal: 最终交付不是聊天答案，而是一份可审计 memo。

Memo sections:

```text
[x] Executive summary
[x] Key claims
[x] Evidence table
[x] Numeric reconciliation
[x] Cross-document contradictions
[x] Risk flags
[x] Unsupported or weakly supported claims
[x] Confidence and limitations
```

Each conclusion must include:

```text
[x] citation
[x] source document
[x] page/section
[x] metric
[x] period
[x] validator result
```

Acceptance criteria:

```text
[x] user can trace every conclusion to source evidence
[x] numbers can be recomputed
[x] unresolved issues are explicit
[x] memo separates evidence from inference
```

## 8. Killer Experiment

**Experiment: Ordinary RAG vs Evidence Engine on financial due-diligence tasks.**

Methods:

```text
naive PDF RAG
hybrid retrieval + reranker
GraphRAG
full evidence engine
```

Tasks:

```text
cross-year financial trend
cross-company comparison
claim verification
chart/table reconciliation
risk contradiction detection
```

Compare:

```text
citation correctness
numeric correctness
fiscal-period correctness
unsupported-claim rate
contradiction detection
answer faithfulness
```

Expected conclusion:

```text
Ordinary RAG generates fluent answers but often confuses fiscal periods, numbers, and citations.
The evidence engine reduces unsupported claims and numeric mismatches through graph retrieval, financial normalization, and validators.
```

## 9. Final Report Outline

```text
1. Problem framing: financial AI needs auditable evidence
2. Data sources and document registry
3. Multimodal extraction pipeline
4. Financial normalization layer
5. Evidence graph
6. Claim decomposition and verification
7. Due-diligence task set
8. Baselines and ablations
9. Main results
10. Failure taxonomy
11. Example due-diligence memo
12. Reproducibility guide
```

Key figures:

```text
pipeline architecture
evidence graph example
citation correctness by method
numeric mismatch rate by method
unsupported-claim rate by method
period-confusion errors
ablation table
contradiction detection examples
sample memo
```

## 10. Resume Bullet

Long version:

> Built a multimodal financial due-diligence evidence engine combining SEC/FMP data, earnings transcripts, investor decks, GraphRAG, table/chart extraction, and claim-level validators to reconcile financial narratives, detect unsupported claims, numeric mismatches, fiscal-period errors, and cross-document contradictions.

Short version:

> Built a multimodal financial evidence engine that verifies due-diligence claims across SEC filings, transcripts, tables, and investor-deck charts using GraphRAG, numeric reconciliation, and citation validators.
