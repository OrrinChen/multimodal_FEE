"""Document extraction package."""

from financial_evidence_engine.extraction.models import EvidenceUnit, SourceSpan
from financial_evidence_engine.extraction.table_extractor import extract_markdown_table
from financial_evidence_engine.extraction.text_extractor import extract_10k_sections, html_to_text
from financial_evidence_engine.extraction.transcript_parser import extract_transcript_sections
from financial_evidence_engine.extraction.xbrl_extractor import extract_xbrl_facts

__all__ = [
    "EvidenceUnit",
    "SourceSpan",
    "extract_10k_sections",
    "extract_markdown_table",
    "extract_transcript_sections",
    "extract_xbrl_facts",
    "html_to_text",
]
