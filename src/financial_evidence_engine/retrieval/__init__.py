"""Evidence retrieval package."""

from .real_baselines import (
    BM25EvidenceRetriever,
    DenseEvidenceRetriever,
    GraphEvidenceRetriever,
    HybridEvidenceRetriever,
    REAL_RETRIEVAL_METHODS,
    RealRetrievalEvaluationResult,
    RetrievalCorpus,
    RetrievalCorpusDocument,
    RetrievalFailureCase,
    RetrievalResult,
    build_retrieval_corpus,
    run_real_retrieval_evaluation,
)
from .raw_corpus import (
    ChunkIndexManifest,
    ChunkProvenance,
    CorpusVersionManifest,
    DocumentChunk,
    RawCorpusBuilder,
    RawFinancialCorpus,
    build_raw_financial_corpus,
)

__all__ = [
    "BM25EvidenceRetriever",
    "ChunkIndexManifest",
    "ChunkProvenance",
    "CorpusVersionManifest",
    "DenseEvidenceRetriever",
    "DocumentChunk",
    "GraphEvidenceRetriever",
    "HybridEvidenceRetriever",
    "REAL_RETRIEVAL_METHODS",
    "RawCorpusBuilder",
    "RawFinancialCorpus",
    "RealRetrievalEvaluationResult",
    "RetrievalCorpus",
    "RetrievalCorpusDocument",
    "RetrievalFailureCase",
    "RetrievalResult",
    "build_raw_financial_corpus",
    "build_retrieval_corpus",
    "run_real_retrieval_evaluation",
]
