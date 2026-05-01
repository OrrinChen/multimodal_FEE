"""Smoke check for real local retrieval evaluation runs."""

from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from financial_evidence_engine.evaluation import build_seed_task_set
from financial_evidence_engine.retrieval import run_real_retrieval_evaluation


def main() -> None:
    result = run_real_retrieval_evaluation(build_seed_task_set())
    full = result.reports["full_engine_real"]
    bm25 = result.reports["bm25_real"]
    print(
        f"tasks={result.task_count} "
        f"corpus_documents={result.corpus_document_count} "
        f"methods={len(result.reports)} "
        f"bm25_numeric_correctness={bm25.metrics['numeric_correctness']} "
        f"full_verdict_accuracy={full.metrics['verdict_accuracy']} "
        f"failure_cases={len(result.failure_cases)}"
    )


if __name__ == "__main__":
    main()
