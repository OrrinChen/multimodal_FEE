"""Evaluation package."""

from .baselines import (
    Phase7EvaluationReport,
    build_phase7_evaluation_report,
    run_ablation_evaluations,
    run_baseline_evaluations,
)
from .gold_builder import build_seed_task_set
from .metrics import EvaluationReport, EvaluationRun, RetrievedEvidence, TaskPrediction, evaluate_run
from .task_set import (
    DueDiligenceTask,
    DueDiligenceTaskSet,
    EvidenceRequirement,
    KnownDistractor,
    NumericCheckSpec,
)

__all__ = [
    "DueDiligenceTask",
    "DueDiligenceTaskSet",
    "EvidenceRequirement",
    "EvaluationReport",
    "EvaluationRun",
    "KnownDistractor",
    "NumericCheckSpec",
    "Phase7EvaluationReport",
    "RetrievedEvidence",
    "TaskPrediction",
    "build_phase7_evaluation_report",
    "build_seed_task_set",
    "evaluate_run",
    "run_ablation_evaluations",
    "run_baseline_evaluations",
]
