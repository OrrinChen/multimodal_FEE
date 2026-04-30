# Task Memory: Multimodal Financial Due-Diligence Evidence Engine

## Latest Status

Current branch:

```text
codex/ashare-radar-phase1a
```

Latest commit:

```text
Phase 0 skeleton commit in this repository history.
```

Current phase:

```text
Phase 1: document registry and ingestion
```

Main blocker:

```text
SEC/XBRL ingestion has not been implemented yet.
```

Next recommended action:

```text
Implement the SEC/XBRL document registry for the initial 3-company universe.
```

Latest workflow update:

```text
Completed Phase 0 repository skeleton.

Added the standard Codex automation workflow files:
- AGENTS.md
- README.md
- VALIDATION.md
- RUNBOOK.md

Added project skeleton:
- .gitignore
- pyproject.toml
- configs/companies.yaml
- placeholder config files for future phases
- src/financial_evidence_engine/ package layout
- tests/test_phase0_skeleton.py

ROADMAP.md now has a Current State and Automation Workflow section.
This lets future Codex runs identify the current phase, deferred work, validation commands, and next recommended action without re-reading chat history.
```

Latest validation:

```text
Passed:
- required workflow files exist
- git diff --check
- markdown trailing-whitespace scan
- python3 -m compileall src
- python3 -m pytest
- config smoke check loaded ['AAPL', 'MSFT', 'NVDA']

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

The only implementation code so far is a small configuration loader for the initial company universe. SEC ingestion, extraction, retrieval, graph construction, and claim verification are not implemented yet.

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
[ ] Implement SEC client
[ ] Implement FMP client
[ ] Implement document registry
[ ] Implement cache/version hash
[ ] Store filing metadata
[ ] Store transcript metadata
[ ] Store investor deck metadata
```

### Step 3: Extraction Layer

```text
[ ] Extract filing text
[ ] Split filing sections
[ ] Parse XBRL facts
[ ] Parse transcripts
[ ] Extract tables
[ ] Add deck PDF parsing
[ ] Add chart extraction only after table/text pipeline works
```

### Step 4: Normalization Layer

```text
[ ] Entity linker
[ ] Ticker/CIK resolver
[ ] Fiscal period resolver
[ ] Metric alias mapper
[ ] Unit normalizer
[ ] Currency normalizer
[ ] Annual vs quarterly guardrails
```

### Step 5: Evidence Graph

```text
[ ] Define graph nodes
[ ] Define graph edges
[ ] Build graph from documents and evidence units
[ ] Link claims to evidence units
[ ] Link metrics across documents
[ ] Track risk themes across years
```

### Step 6: Claim Verification

```text
[ ] Claim decomposer
[ ] Evidence selector
[ ] Numeric reconciler
[ ] Citation validator
[ ] Fiscal-period validator
[ ] Contradiction detector
[ ] Verdict generator
```

### Step 7: Evaluation

```text
[ ] Build 50-100 task gold set
[ ] Implement metrics
[ ] Implement BM25 baseline
[ ] Implement dense/hybrid baseline
[ ] Implement GraphRAG baseline
[ ] Implement full-system run
[ ] Run ablations
```

### Step 8: Final Report

```text
[ ] Generate due-diligence memo example
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
