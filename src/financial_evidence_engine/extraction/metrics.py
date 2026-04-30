"""Metric and unit normalization helpers for early extraction."""

from __future__ import annotations

from typing import Optional, Tuple


DEFAULT_METRIC_ALIASES = {
    "revenue": "revenue",
    "revenues": "revenue",
    "net sales": "revenue",
    "sales": "revenue",
    "us-gaap:revenues": "revenue",
    "operating income": "operating_income",
    "operatingincomeloss": "operating_income",
    "us-gaap:operatingincomeloss": "operating_income",
    "net income": "net_income",
    "netincomeloss": "net_income",
    "us-gaap:netincomeloss": "net_income",
    "cash flow from operations": "operating_cash_flow",
    "netcashprovidedbyusedinoperatingactivities": "operating_cash_flow",
    "us-gaap:netcashprovidedbyusedinoperatingactivities": "operating_cash_flow",
}


def normalize_metric(raw_metric: str) -> Optional[str]:
    key = raw_metric.strip().lower().replace("_", " ")
    compact_key = raw_metric.strip().lower().replace("_", "").replace(" ", "")
    return DEFAULT_METRIC_ALIASES.get(key) or DEFAULT_METRIC_ALIASES.get(compact_key)


def parse_unit_and_currency(raw_unit: str) -> Tuple[Optional[str], Optional[str]]:
    tokens = raw_unit.strip().split()
    if not tokens:
        return None, None

    currency = tokens[0].upper() if tokens[0].upper() in {"USD", "EUR", "GBP", "JPY", "CNY"} else None
    if currency:
        unit = " ".join(tokens[1:]) or currency
    else:
        unit = raw_unit.strip()
    return unit or None, currency
