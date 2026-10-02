"""
Financial sentiment analysis module.
Computes a normalized sentiment score between -1.0 and +1.0 along with human-readable labels.
Uses domain-adapted financial polarity dictionaries and negation handling.
"""

import re
from typing import Dict, Any, Tuple

# Domain financial lexicons adapted from financial analysis benchmarks
POSITIVE_WORDS = {
    "growth": 0.8, "profit": 0.9, "bullish": 0.9, "beat": 0.8, "outperform": 0.9,
    "expansion": 0.7, "gain": 0.7, "soar": 0.9, "dividend": 0.6, "rebound": 0.7,
    "exceptional": 0.9, "promising": 0.7, "record": 0.8, "solid": 0.7, "surge": 0.8,
    "upside": 0.7, "upgrade": 0.8, "recovery": 0.7, "sustainable": 0.6, "innovative": 0.7,
    "milestone": 0.6, "rally": 0.8, "profitable": 0.8, "strong": 0.7, "success": 0.8
}

NEGATIVE_WORDS = {
    "loss": -0.8, "decline": -0.7, "bearish": -0.8, "miss": -0.7, "underperform": -0.8,
    "downgrade": -0.9, "probe": -0.8, "investigation": -0.8, "irregularities": -0.9,
    "disruption": -0.8, "penalty": -0.8, "fine": -0.7, "sanctions": -0.9, "halt": -0.7,
    "default": -1.0, "bankruptcy": -1.0, "slump": -0.8, "plunge": -0.9, "crisis": -0.9,
    "squeeze": -0.7, "bottleneck": -0.7, "alarming": -0.8, "spik": -0.5, "debt": -0.5,
    "fall": -0.6, "drop": -0.6, "inflation": -0.6, "warning": -0.8, "deficit": -0.7
}

INTENSIFIERS = {
    "very": 1.3, "extremely": 1.5, "severely": 1.5, "massively": 1.5,
    "sharply": 1.4, "deeply": 1.4, "exceptionally": 1.4, "substantially": 1.3
}

NEGATIONS = {"not", "no", "never", "hardly", "barely", "scarcely", "without"}

def extract_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyzes text and returns:
    - sentiment_score: float in [-1.0, 1.0]
    - sentiment_label: "Positive" | "Neutral" | "Negative"
    """
    if not text or not text.strip():
        return {
            "sentiment_score": 0.0,
            "sentiment_label": "Neutral"
        }

    # Tokenize words while lowercasing
    tokens = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    if not tokens:
        return {
            "sentiment_score": 0.0,
            "sentiment_label": "Neutral"
        }

    total_weight = 0.0
    matched_words = 0

    for i, token in enumerate(tokens):
        score = 0.0
        # Check positive
        if token in POSITIVE_WORDS:
            score = POSITIVE_WORDS[token]
        elif any(token.startswith(k) for k in POSITIVE_WORDS):
            k = next(k for k in POSITIVE_WORDS if token.startswith(k))
            score = POSITIVE_WORDS[k]
        # Check negative
        elif token in NEGATIVE_WORDS:
            score = NEGATIVE_WORDS[token]
        elif any(token.startswith(k) for k in NEGATIVE_WORDS):
            k = next(k for k in NEGATIVE_WORDS if token.startswith(k))
            score = NEGATIVE_WORDS[k]

        if score != 0.0:
            # Check for negation in preceding 2 tokens
            preceding = tokens[max(0, i - 2):i]
            is_negated = any(neg in preceding for neg in NEGATIONS)
            if is_negated:
                score = -0.7 * score  # Invert with slight dampening

            # Check for intensifier in preceding 1 token
            if i > 0 and tokens[i - 1] in INTENSIFIERS:
                score *= INTENSIFIERS[tokens[i - 1]]

            total_weight += score
            matched_words += 1

    if matched_words == 0:
        final_score = 0.0
    else:
        # Average and apply soft hyperbolic dampening to bound nicely in [-1.0, 1.0]
        raw_avg = total_weight / (matched_words ** 0.5)
        # Normalize and strictly clamp between -1.0 and 1.0
        final_score = max(-1.0, min(1.0, round(raw_avg / 1.5, 2)))

    # Determine human-readable label
    if final_score >= 0.15:
        label = "Positive"
    elif final_score <= -0.15:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "sentiment_score": final_score,
        "sentiment_label": label
    }
