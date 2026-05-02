"""Claim reasoning and verification package."""

from financial_evidence_engine.reasoning.claim_decomposer import ClaimDecomposer
from financial_evidence_engine.reasoning.claim_verifier import ClaimVerifier
from financial_evidence_engine.reasoning.contradiction_detector import ContradictionDetector
from financial_evidence_engine.reasoning.evidence_selector import EvidenceSelector
from financial_evidence_engine.reasoning.llm_decomposition import (
    ClaimDecompositionProvider,
    DecompositionArtifactManifest,
    DecompositionCandidate,
    DecompositionComparisonExample,
    DecompositionComparisonReport,
    DecompositionSchemaError,
    DecompositionTrace,
    LiveLLMUnavailable,
    OptionalLiveLLMClaimDecomposer,
    RecordedLLMClaimDecomposer,
    RuleBasedClaimDecomposer,
    ValidatorGate,
    build_decomposition_comparison_report,
    write_decomposition_comparison_artifacts,
)
from financial_evidence_engine.reasoning.models import (
    Claim,
    ClaimVerificationResult,
    EvidenceReference,
    Subclaim,
    SubclaimVerification,
    ValidatorCheck,
    Verdict,
)

__all__ = [
    "Claim",
    "ClaimDecompositionProvider",
    "ClaimDecomposer",
    "ClaimVerificationResult",
    "ClaimVerifier",
    "ContradictionDetector",
    "DecompositionArtifactManifest",
    "DecompositionCandidate",
    "DecompositionComparisonExample",
    "DecompositionComparisonReport",
    "DecompositionSchemaError",
    "DecompositionTrace",
    "EvidenceReference",
    "EvidenceSelector",
    "LiveLLMUnavailable",
    "OptionalLiveLLMClaimDecomposer",
    "RecordedLLMClaimDecomposer",
    "RuleBasedClaimDecomposer",
    "Subclaim",
    "SubclaimVerification",
    "ValidatorGate",
    "ValidatorCheck",
    "Verdict",
    "build_decomposition_comparison_report",
    "write_decomposition_comparison_artifacts",
]
