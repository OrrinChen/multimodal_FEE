# RUNBOOK.md

Common commands and operating notes for this repository.

## Orientation

```bash
pwd
```

```bash
git status --short --branch
```

```bash
find . -maxdepth 2 -type f | sort
```

## Read Project State

```bash
sed -n '1,220p' ROADMAP.md
```

```bash
sed -n '1,220p' TASK_MEMORY.md
```

```bash
sed -n '1,220p' VALIDATION.md
```

## Validation

```bash
git diff --check
```

```bash
awk '/[ \t]$/ {print FILENAME ":" FNR ": trailing whitespace"; bad=1} END {exit bad}' *.md
```

```bash
if [ -d src ]; then python3 -m compileall src scripts; else echo "SKIP compileall: src/ not created yet"; fi
```

```bash
if [ -d tests ]; then python3 -m pytest; else echo "SKIP pytest: tests/ not created yet"; fi
```

```bash
python3 - <<'PY'
from pathlib import Path
import sys

sys.path.insert(0, "src")
from financial_evidence_engine.config import load_company_universe

companies = load_company_universe(Path("configs/companies.yaml"))
print([company.ticker for company in companies])
PY
```

```bash
python3 scripts/smoke_phase1_registry.py
```

```bash
python3 scripts/smoke_phase2_extraction.py
```

```bash
python3 scripts/smoke_real_retrieval_evaluation.py
```

```bash
python3 scripts/smoke_case_studies.py
```

```bash
python3 scripts/smoke_deck_chart_extraction.py
```

```bash
python3 scripts/smoke_raw_corpus.py
```

```bash
python3 scripts/smoke_real_retrieval_evaluation.py --corpus raw
```

```bash
python3 scripts/smoke_embedding_backend.py
```

```bash
python3 scripts/smoke_llm_decomposition.py
```

```bash
python3 scripts/smoke_narrative_causal.py
```

## Development Notes

- Keep early work focused on a narrow vertical slice.
- Start with SEC/XBRL and validated numeric claims before adding transcripts, investor decks, charts, or GraphRAG complexity.
- Prefer real retrieval and failure-case evidence before expanding UI, dashboards, or broad GraphRAG experiments.
- Treat downloaded data and API responses as reproducible artifacts with source metadata, retrieval time, and version hashes.
- Never commit credentials, paid API keys, private filings, or local-only data.

## Troubleshooting

If validation fails:

1. Reproduce the failing command directly.
2. Inspect the smallest relevant file or test.
3. Fix the root cause, not just the symptom.
4. Rerun the failed command.
5. Rerun `git diff --check`.
6. Record the result in `TASK_MEMORY.md`.

If external credentials are required:

1. Stop before adding or hardcoding secrets.
2. Document the missing variable name.
3. Add `.env.example` only when the project has a real runtime that needs it.
4. Ask the user for approval before requiring paid services.
