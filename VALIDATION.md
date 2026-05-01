# VALIDATION.md

Use this file as the source of truth for validation commands.

## Always Run

Run these commands before reporting completion:

```bash
git status --short --branch
```

```bash
test -f AGENTS.md && test -f README.md && test -f ROADMAP.md && test -f TASK_MEMORY.md && test -f VALIDATION.md && test -f RUNBOOK.md
```

```bash
git diff --check
```

```bash
awk '/[ \t]$/ {print FILENAME ":" FNR ": trailing whitespace"; bad=1} END {exit bad}' *.md
```

## Python Validation

Run these once Python source or tests exist:

```bash
if [ -d src ]; then python3 -m compileall src scripts; else echo "SKIP compileall: src/ not created yet"; fi
```

```bash
if [ -d tests ]; then python3 -m pytest; else echo "SKIP pytest: tests/ not created yet"; fi
```

## Config Smoke Checks

Run this once `configs/companies.yaml` and the Python package exist:

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

## Phase 1 Registry Smoke Check

Run this once the SEC/XBRL document registry exists:

```bash
python3 scripts/smoke_phase1_registry.py
```

## Phase 2 Extraction Smoke Check

Run this once extraction modules exist:

```bash
python3 scripts/smoke_phase2_extraction.py
```

## Phase 3 Normalization Smoke Check

Run this once normalization modules exist:

```bash
python3 scripts/smoke_phase3_normalization.py
```

## Phase-Specific Validation

For each phase, run the phase acceptance checks listed in `ROADMAP.md`.

Required smoke checks should be added here when new entry points are created:

- CLI commands
- data ingestion commands
- extraction scripts
- evaluation scripts
- report generation scripts

When a check is skipped, record the reason in `TASK_MEMORY.md`.
