"""Report generation package."""

from .final_report import (
    ChartSpec,
    FinalReportPackage,
    REPRODUCIBILITY_COMMANDS,
    ReportTable,
    build_final_report_package,
)
from .memo import (
    DueDiligenceMemo,
    EvidenceTableRow,
    MemoClaim,
    MemoConclusion,
    MemoIssue,
    NumericReconciliationRow,
    build_due_diligence_memo,
)
from .portfolio_report import (
    FigureSpec,
    PortfolioReportArtifactManifest,
    PortfolioReportPackage,
    PortfolioReportSection,
    TableSpec,
    build_portfolio_report_package,
    write_portfolio_report_artifacts,
)

__all__ = [
    "ChartSpec",
    "DueDiligenceMemo",
    "EvidenceTableRow",
    "FigureSpec",
    "FinalReportPackage",
    "MemoClaim",
    "MemoConclusion",
    "MemoIssue",
    "NumericReconciliationRow",
    "PortfolioReportArtifactManifest",
    "PortfolioReportPackage",
    "PortfolioReportSection",
    "REPRODUCIBILITY_COMMANDS",
    "ReportTable",
    "TableSpec",
    "build_due_diligence_memo",
    "build_final_report_package",
    "build_portfolio_report_package",
    "write_portfolio_report_artifacts",
]
