"""
Prototype Risk Impact Scoring Module.
Calculates an interpretable 1–10 impact score based on:
1. Event Category Systemic Risk Weight
2. Sentiment Directionality and Intensity
3. Severity Terminology Multipliers
4. Risk Level Categorization (Low, Moderate, High, Critical)
"""

import re
from typing import Dict, Any

# Systemic risk baseline weights by event category (1 to 10 scale)
EVENT_BASE_IMPACT = {
    "Geopolitical": 7.0,
    "Credit Event": 6.5,
    "Regulatory": 6.0,
    "Macroeconomic": 5.5,
    "Merger/Acquisition": 4.5,
    "Earnings/Financial": 4.0,
    "Product Launch": 3.0,
    "Other": 3.0
}

SEVERITY_KEYWORDS = {
    "default": 2.5, "bankruptcy": 2.5, "insolvency": 2.5, "sanctions": 2.0,
    "war": 2.0, "conflict": 1.5, "probe": 1.5, "investigation": 1.5,
    "liquidity crisis": 2.0, "irregularities": 1.5, "halt": 1.5,
    "disruption": 1.2, "downgrade": 1.5, "penalty": 1.0, "restructuring": 1.0
}

def map_impact_to_level(impact_score: int) -> str:
    """Maps 1-10 impact score to human-readable risk classification."""
    if impact_score >= 9:
        return "Critical"
    elif impact_score >= 7:
        return "High"
    elif impact_score >= 4:
        return "Moderate"
    else:
        return "Low"

def calculate_impact(sentiment_score: float, event_type: str, text: str = "") -> Dict[str, Any]:
    """
    Computes Prototype Risk Impact Score (1-10) and Risk Level.
    """
    base_impact = EVENT_BASE_IMPACT.get(event_type, 3.5)

    # Directional sentiment adjustment:
    # Highly negative sentiment (-1.0) increases risk by up to +2.5 points.
    # Positive sentiment (+1.0) decreases risk by up to -2.0 points.
    if sentiment_score < 0:
        sentiment_delta = abs(sentiment_score) * 2.5
    else:
        sentiment_delta = -1.0 * sentiment_score * 2.0

    # Severity keyword additions
    severity_boost = 0.0
    lower_text = text.lower() if text else ""
    for kw, boost in SEVERITY_KEYWORDS.items():
        if kw in lower_text:
            severity_boost += boost

    # Cap severity boost so it doesn't arbitrarily skew isolated events
    severity_boost = min(3.0, severity_boost)

    # Total raw score
    raw_score = base_impact + sentiment_delta + severity_boost

    # Bound strictly between 1 and 10
    final_score = int(max(1, min(10, round(raw_score))))
    risk_level = map_impact_to_level(final_score)

    return {
        "impact_score": final_score,
        "risk_level": risk_level,
        "is_stress_test_trigger": final_score >= 7
    }
