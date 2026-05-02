"""Final report packaging for the financial evidence engine."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Mapping, Tuple

from financial_evidence_engine.evaluation import Phase7EvaluationReport

from .memo import DueDiligenceMemo


FINAL_REPORT_TITLE = "Multimodal Financial Due-Diligence Evidence Engine Final Report"

REPORT_OUTLINE: Tuple[str, ...] = (
    "Problem framing: financial AI needs auditable evidence",
    "Data sources and document registry",
    "Multimodal extraction pipeline",
    "Financial normalization layer",
    "Evidence graph",
    "Claim decomposition and verification",
    "Due-diligence task set",
    "Baselines and ablations",
    "Main results",
    "Failure taxonomy",
    "Example due-diligence memo",
    "Reproducibility guide",
)

REPRODUCIBILITY_COMMANDS: Tuple[str, ...] = (
    "python3 -m compileall src scripts",
    "python3 -m pytest",
    "python3 scripts/smoke_phase1_registry.py",
    "python3 scripts/smoke_phase2_extraction.py",
    "python3 scripts/smoke_phase3_normalization.py",
    "python3 scripts/smoke_phase4_evidence_graph.py",
    "python3 scripts/smoke_phase5_claim_verification.py",
    "python3 scripts/smoke_phase6_task_set.py",
    "python3 scripts/smoke_phase7_evaluation.py",
    "python3 scripts/smoke_real_retrieval_evaluation.py",
    "python3 scripts/smoke_case_studies.py",
    "python3 scripts/smoke_deck_chart_extraction.py",
    "python3 scripts/smoke_raw_corpus.py",
    "python3 scripts/smoke_embedding_backend.py",
    "python3 scripts/smoke_phase8_memo.py",
    "python3 scripts/smoke_final_report_package.py",
)

RESUME_BULLET_LONG = (
    "Built a multimodal financial due-diligence evidence engine combining SEC/FMP data, "
    "earnings transcripts, investor decks, GraphRAG, table/chart extraction, and "
    "claim-level validators to reconcile financial narratives, detect unsupported claims, "
    "numeric mismatches, fiscal-period errors, and cross-document contradictions."
)

RESUME_BULLET_SHORT = (
    "Built a multimodal financial evidence engine that verifies due-diligence claims across "
    "SEC filings, transcripts, tables, and investor-deck charts using GraphRAG, numeric "
    "reconciliation, and citation validators."
)


@dataclass(frozen=True)
class ChartSpec:
    """Portable chart data for the final report."""

    chart_id: str
    title: str
    metric: str
    values: Mapping[str, Decimal]
    insight: str

    def to_dict(self) -> Mapping[str, object]:
        return {
            "chart_id": self.chart_id,
            "title": self.title,
            "metric": self.metric,
            "values": {name: str(value) for name, value in self.values.items()},
            "insight": self.insight,
        }


@dataclass(frozen=True)
class ReportTable:
    """Portable table data for the final report."""

    table_id: str
    title: str
    columns: Tuple[str, ...]
    rows: Tuple[Mapping[str, object], ...]

    def to_dict(self) -> Mapping[str, object]:
        return {
            "table_id": self.table_id,
            "title": self.title,
            "columns": list(self.columns),
            "rows": [_stringify_row(row) for row in self.rows],
        }


@dataclass(frozen=True)
class FinalReportPackage:
    """All final-report artifacts in one serializable package."""

    title: str
    task_count: int
    outline: Tuple[str, ...]
    charts: Tuple[ChartSpec, ...]
    tables: Tuple[ReportTable, ...]
    sample_memo: DueDiligenceMemo
    reproducibility_commands: Tuple[str, ...]
    resume_bullet_long: str
    resume_bullet_short: str

    def to_dict(self) -> Mapping[str, object]:
        return {
            "title": self.title,
            "task_count": self.task_count,
            "outline": list(self.outline),
            "charts": [chart.to_dict() for chart in self.charts],
            "tables": [table.to_dict() for table in self.tables],
            "sample_memo": self.sample_memo.to_dict(),
            "reproducibility_commands": list(self.reproducibility_commands),
            "resume_bullet_long": self.resume_bullet_long,
            "resume_bullet_short": self.resume_bullet_short,
        }

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", ""]
        for index, section in enumerate(self.outline, start=1):
            lines.extend([f"## {index}. {section}", ""])
            lines.extend(_section_lines(section, self))
            lines.append("")
        lines.extend(["## Resume bullet", "", self.resume_bullet_long, "", self.resume_bullet_short])
        return "\n".join(lines).rstrip() + "\n"


def build_final_report_package(
    phase7_report: Phase7EvaluationReport,
    sample_memo: DueDiligenceMemo,
) -> FinalReportPackage:
    """Build final report charts, tables, sample memo, and reproducibility notes."""

    charts = _build_charts(phase7_report)
    tables = _build_tables(phase7_report)
    return FinalReportPackage(
        title=FINAL_REPORT_TITLE,
        task_count=phase7_report.task_count,
        outline=REPORT_OUTLINE,
        charts=charts,
        tables=tables,
        sample_memo=sample_memo,
        reproducibility_commands=REPRODUCIBILITY_COMMANDS,
        resume_bullet_long=RESUME_BULLET_LONG,
        resume_bullet_short=RESUME_BULLET_SHORT,
    )


def _build_charts(phase7_report: Phase7EvaluationReport) -> Tuple[ChartSpec, ...]:
    baseline_reports = phase7_report.baseline_reports
    return (
        ChartSpec(
            chart_id="citation_correctness_by_method",
            title="Citation correctness by method",
            metric="citation_exactness",
            values=_metric_values(baseline_reports, "citation_exactness"),
            insight="Full evidence engine keeps citations tied to validated evidence rows.",
        ),
        ChartSpec(
            chart_id="numeric_mismatch_rate_by_method",
            title="Numeric mismatch rate by method",
            metric="1 - numeric_correctness",
            values=_inverted_metric_values(baseline_reports, "numeric_correctness"),
            insight="Numeric validators reduce mismatch rate versus retrieval-only baselines.",
        ),
        ChartSpec(
            chart_id="unsupported_claim_rate_by_method",
            title="Unsupported-claim rate by method",
            metric="unsupported_claim_rate",
            values=_metric_values(baseline_reports, "unsupported_claim_rate"),
            insight="Unsupported claims remain visible instead of being hidden in fluent answers.",
        ),
        ChartSpec(
            chart_id="period_confusion_errors_by_method",
            title="Period-confusion errors by method",
            metric="1 - fiscal_period_correctness",
            values=_inverted_metric_values(baseline_reports, "fiscal_period_correctness"),
            insight="Fiscal-period validation catches year and quarter confusion.",
        ),
    )


def _build_tables(phase7_report: Phase7EvaluationReport) -> Tuple[ReportTable, ...]:
    return (
        _baseline_metrics_table(phase7_report),
        _ablation_metrics_table(phase7_report),
        ReportTable(
            table_id="reproducibility_commands",
            title="Reproducibility commands",
            columns=("step", "command"),
            rows=tuple(
                {"step": index, "command": command}
                for index, command in enumerate(REPRODUCIBILITY_COMMANDS, start=1)
            ),
        ),
    )


def _baseline_metrics_table(phase7_report: Phase7EvaluationReport) -> ReportTable:
    rows = []
    for method, report in phase7_report.baseline_reports.items():
        rows.append(
            {
                "method": method,
                "evidence_recall_at_k": report.metrics["evidence_recall_at_k"],
                "citation_exactness": report.metrics["citation_exactness"],
                "numeric_correctness": report.metrics["numeric_correctness"],
                "fiscal_period_correctness": report.metrics["fiscal_period_correctness"],
                "unsupported_claim_rate": report.metrics["unsupported_claim_rate"],
                "verdict_accuracy": report.metrics["verdict_accuracy"],
            }
        )
    return ReportTable(
        table_id="baseline_metrics",
        title="Baseline metrics",
        columns=(
            "method",
            "evidence_recall_at_k",
            "citation_exactness",
            "numeric_correctness",
            "fiscal_period_correctness",
            "unsupported_claim_rate",
            "verdict_accuracy",
        ),
        rows=tuple(rows),
    )


def _ablation_metrics_table(phase7_report: Phase7EvaluationReport) -> ReportTable:
    rows = []
    for method, report in phase7_report.ablation_reports.items():
        rows.append(
            {
                "method": method,
                "evidence_recall_at_k": report.metrics["evidence_recall_at_k"],
                "numeric_correctness": report.metrics["numeric_correctness"],
                "fiscal_period_correctness": report.metrics["fiscal_period_correctness"],
                "contradiction_detection_accuracy": report.metrics["contradiction_detection_accuracy"],
            }
        )
    return ReportTable(
        table_id="ablation_metrics",
        title="Ablation metrics",
        columns=(
            "method",
            "evidence_recall_at_k",
            "numeric_correctness",
            "fiscal_period_correctness",
            "contradiction_detection_accuracy",
        ),
        rows=tuple(rows),
    )


def _metric_values(reports: Mapping[str, object], metric: str) -> Mapping[str, Decimal]:
    return {method: report.metrics[metric] for method, report in reports.items()}


def _inverted_metric_values(reports: Mapping[str, object], metric: str) -> Mapping[str, Decimal]:
    return {method: Decimal("1") - report.metrics[metric] for method, report in reports.items()}


def _section_lines(section: str, package: FinalReportPackage) -> list:
    if section == "Problem framing: financial AI needs auditable evidence":
        return [
            "Financial due diligence needs source-backed answers, not fluent unsupported summaries.",
            "The engine verifies claims through evidence selection, normalization, validators, and memo output.",
        ]
    if section == "Data sources and document registry":
        return [
            "SEC/XBRL remains the authoritative source for filing truth.",
            "FMP is treated as secondary context for transcripts, estimates, and market context.",
        ]
    if section == "Multimodal extraction pipeline":
        return [
            "The local slice normalizes filing text, XBRL facts, transcripts, markdown tables, and one investor-deck chart fixture into evidence units.",
            "Phase 11 adds raw SEC paragraphs, transcript turns, XBRL facts, deck pages, and deck chart chunks for raw-corpus retrieval.",
        ]
    if section == "Financial normalization layer":
        return [
            "Company, metric, period, unit, and currency guardrails prevent accidental apples-to-oranges comparisons.",
        ]
    if section == "Evidence graph":
        return [
            "Evidence graph links companies, documents, periods, metrics, claims, evidence units, and risk themes.",
        ]
    if section == "Claim decomposition and verification":
        return [
            "Claims are decomposed into validator-readable subclaims with citation, period, source, and numeric checks.",
        ]
    if section == "Due-diligence task set":
        return [f"The seed task set contains {package.task_count} multimodal due-diligence task specs."]
    if section == "Baselines and ablations":
        return _table_markdown(package.tables[0]) + [""] + _table_markdown(package.tables[1]) + [
            "",
            "Phase 12 separates deterministic dense_proxy retrieval from optional dense_real and hybrid_real backends.",
        ]
    if section == "Main results":
        lines = []
        for chart in package.charts:
            lines.append(f"- {chart.title}: {chart.insight}")
        return lines
    if section == "Failure taxonomy":
        return [
            "Observed failure classes: wrong citation, numeric mismatch, fiscal-period confusion, entity mismatch, unsupported claim, missed contradiction.",
        ]
    if section == "Example due-diligence memo":
        return package.sample_memo.to_markdown().rstrip().splitlines()
    if section == "Reproducibility guide":
        return [f"- `{command}`" for command in package.reproducibility_commands]
    return []


def _table_markdown(table: ReportTable) -> list:
    lines = [f"### {table.title}"]
    lines.append("| " + " | ".join(table.columns) + " |")
    lines.append("| " + " | ".join("---" for _ in table.columns) + " |")
    for row in table.rows:
        lines.append("| " + " | ".join(str(row[column]) for column in table.columns) + " |")
    return lines


def _stringify_row(row: Mapping[str, object]) -> Mapping[str, object]:
    return {
        key: str(value) if isinstance(value, Decimal) else value
        for key, value in row.items()
    }
