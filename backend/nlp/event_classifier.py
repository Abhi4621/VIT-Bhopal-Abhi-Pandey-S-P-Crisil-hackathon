"""
Event classification module for financial news and social media.
Classifies text into 8 financial categories with an interpretable confidence score:
1. Geopolitical
2. Macroeconomic
3. Credit Event
4. Merger/Acquisition
5. Product Launch
6. Regulatory
7. Earnings/Financial
8. Other
"""

import re
from typing import Dict, Any, Tuple

# Domain keyword profiles for financial event categories
EVENT_KEYWORDS = {
    "Geopolitical": [
        "war", "conflict", "sanctions", "geopolitical", "military", "embargo",
        "trade war", "maritime", "freight corridors", "blockade", "cross-border",
        "territory", "straits", "tensions"
    ],
    "Macroeconomic": [
        "inflation", "interest rate", "rate hike", "central bank", "repo rate",
        "monetary policy", "gdp", "recession", "unemployment", "treasury yields",
        "currency depreciation", "fiscal deficit", "basis points"
    ],
    "Credit Event": [
        "default", "downgrade", "credit watch", "negative outlook", "bankruptcy",
        "insolvency", "restructuring", "debt maturity", "liquidity crisis",
        "spread widening", "repayment failure", "leverage", "refinancing costs"
    ],
    "Merger/Acquisition": [
        "merger", "acquisition", "takeover", "acquire", "stake", "buyout",
        "consolidation", "joint venture", "divestiture", "antitrust review", "equity stake"
    ],
    "Product Launch": [
        "launch", "unveil", "release", "platform", "product", "innovation",
        "next-generation", "solution", "rollout", "suite", "feature", "upgrade"
    ],
    "Regulatory": [
        "probe", "investigation", "regulator", "compliance", "sec", "audit",
        "penalty", "fine", "allegations", "lawsuit", "sanction", "antitrust",
        "irregularities", "filing inquiry"
    ],
    "Earnings/Financial": [
        "earnings", "profit", "revenue", "quarterly", "net profit", "ebitda",
        "margin", "dividend", "q1", "q2", "q3", "q4", "guidance", "sales beat"
    ]
}

def classify_event(text: str) -> Dict[str, Any]:
    """
    Classifies text into financial event categories and assigns confidence.
    """
    if not text or not text.strip():
        return {
            "event_type": "Other",
            "confidence": 0.50
        }

    lower_text = text.lower()
    category_scores = {}

    for category, keywords in EVENT_KEYWORDS.items():
        score = 0
        for kw in keywords:
            # Count exact matches or word boundary occurrences
            pattern = r'\b' + re.escape(kw) + r'\b'
            matches = len(re.findall(pattern, lower_text))
            score += matches * 2

            # Secondary substring match if not full token
            if matches == 0 and kw in lower_text:
                score += 1

        if score > 0:
            category_scores[category] = score

    if not category_scores:
        return {
            "event_type": "Other",
            "confidence": 0.40
        }

    # Identify top scored category
    top_category = max(category_scores, key=category_scores.get)
    top_score = category_scores[top_category]
    total_score = sum(category_scores.values())

    # Calculate confidence score between 0.50 and 0.98
    base_confidence = min(0.95, 0.50 + (top_score / total_score) * 0.45)
    # Extra boost if strong multiple keywords found
    if top_score >= 4:
        base_confidence = min(0.98, base_confidence + 0.05)

    return {
        "event_type": top_category,
        "confidence": round(base_confidence, 2)
    }
