# AGENTS.md

You are working on this repository as an autonomous coding agent.

## Project Goal

This project is the Multimodal Financial Due-Diligence Evidence Engine.

Read these files before making changes:

1. `README.md`
2. `ROADMAP.md`
3. `TASK_MEMORY.md`
4. `VALIDATION.md`
5. `RUNBOOK.md`

Your job is to advance the next incomplete roadmap phase. Do not invent unrelated features or change the project direction.

## Project Direction

Build a claim-level financial evidence verification engine for due diligence.

The engine should take financial claims or due-diligence questions and produce auditable verification:

- decomposed subclaims
- supporting evidence
- contradicting evidence
- numeric reconciliation
- citation validation
- fiscal-period validation
- final verdict: `support`, `contradict`, or `insufficient`
- due-diligence memo output

This is not a chatbot, not a generic PDF QA app, and not a general-purpose agent framework.

## Hard Constraints

Do not:

- change project direction without explicit instruction
- expand into generic agent infrastructure
- add heavy dependencies unless justified in `TASK_MEMORY.md`
- rewrite large modules unnecessarily
- hide failing tests, skipped tests, or partial results
- generate misleading evaluation reports
- commit secrets, credentials, tokens, downloaded private files, or local private data
- perform destructive actions without explicit approval
- require paid external services unless the user explicitly approves them
- compare financial results across different fiscal periods, currencies, units, or companies without explicit normalization
- treat citations as decorative text rather than validated evidence

## Workflow

Before starting:

1. Run `git status --short --branch`.
2. Read `ROADMAP.md`.
3. Read `TASK_MEMORY.md`.
4. Read `VALIDATION.md`.
5. Identify the next incomplete phase and its acceptance criteria.
6. Inspect relevant files before editing.

During work:

1. Make small, testable changes.
2. Prefer simple, modular interfaces.
3. Add or update tests when behavior changes.
4. Update `README.md` when user-facing behavior changes.
5. Update `TASK_MEMORY.md` with what changed, what was verified, known limitations, and the next recommended action.
6. Keep roadmap checkboxes current when a phase advances.

Validation:

1. Run the commands listed in `VALIDATION.md`.
2. Always run relevant unit tests when tests exist.
3. Run smoke tests for touched CLI, data, or UI paths.
4. Run `git diff --check`.
5. Report any skipped validation and why it was skipped.

## Commit Rules

Commit only when a coherent phase or subphase is complete and validation has been run.

Use clear commit messages:

- `feat: ...`
- `fix: ...`
- `docs: ...`
- `test: ...`
- `chore: ...`

Before committing:

1. Run `git status --short`.
2. Review `git diff`.
3. Confirm only intended files are staged.
4. Do not stage unrelated files outside this project directory.

## Stopping Rules

Only stop and ask for help if:

- tests cannot pass after reasonable debugging
- product direction is ambiguous
- implementation risks data loss
- credentials, paid APIs, or private data are required
- a task would violate hard constraints
- the git worktree contains unrelated changes that make a safe commit impossible

When stopping, report:

- what was attempted
- what passed
- what failed
- exact blocker
- recommended next step
