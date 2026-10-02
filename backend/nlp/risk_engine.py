"""
Unified Risk Engine pipeline.
Integrates text cleaning, entity detection, sentiment scoring,
event classification, and prototype impact scoring into a structured risk signal.
"""

from typing import Dict, Any, Optional
from datetime import datetime, timezone
import uuid
from backend.ingestion.cleaner import clean_financial_text
from backend.nlp.sentiment import extract_sentiment
from backend.nlp.event_classifier import classify_event
from backend.nlp.impact_score import calculate_impact

# Company canonical entities and recognized aliases
COMPANY_ALIASES = {
    "tata motors": "Tata Motors",
    "tatamotors": "Tata Motors",
    "reliance": "Reliance Industries",
    "reliance industries": "Reliance Industries",
    "ril": "Reliance Industries",
    "hdfc": "HDFC Bank",
    "hdfc bank": "HDFC Bank",
    "adani": "Adani Enterprises",
    "adani enterprises": "Adani Enterprises",
    "icici": "ICICI Bank",
    "icici bank": "ICICI Bank",
    "infosys": "Infosys",
    "infy": "Infosys",
    "tata steel": "Tata Steel",
    "tesla": "Tesla",
    "apple": "Apple",
    "microsoft": "Microsoft"
}

def detect_entity(text: str, fallback_company: Optional[str] = None) -> str:
    """Detects company entity from text or falls back to provided company."""
    if fallback_company and fallback_company.strip():
        lower_fb = fallback_company.lower().strip()
        if lower_fb in COMPANY_ALIASES:
            return COMPANY_ALIASES[lower_fb]
        return fallback_company.strip()

    lower_text = text.lower()
    for alias, canonical in COMPANY_ALIASES.items():
        if alias in lower_text:
            return canonical

    return "General Market"

def analyze_text(text: str, company: Optional[str] = None, source: str = "Direct Ingestion") -> Dict[str, Any]:
    """
    Core pipeline: Text -> Cleaning -> Entity -> Sentiment -> Event -> Impact -> Signal.
    """
    cleaned_text = clean_financial_text(text)
    detected_company = detect_entity(cleaned_text, company)

    # 1. Sentiment analysis
    sentiment_data = extract_sentiment(cleaned_text)
    sentiment_score = sentiment_data["sentiment_score"]
    sentiment_label = sentiment_data["sentiment_label"]

    # 2. Event classification
    event_data = classify_event(cleaned_text)
    event_type = event_data["event_type"]
    confidence = event_data["confidence"]

    # 3. Impact scoring
    impact_data = calculate_impact(sentiment_score, event_type, cleaned_text)
    impact_score = impact_data["impact_score"]
    risk_level = impact_data["risk_level"]
    is_trigger = impact_data["is_stress_test_trigger"]

    # Generate synthetic event summary (first sentence or clipped text)
    sentences = cleaned_text.split(".")
    summary = sentences[0].strip() if sentences else cleaned_text[:120]
    if len(summary) > 140:
        summary = summary[:137] + "..."

    return {
        "id": f"SIG-{uuid.uuid4().hex[:8].upper()}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "company": detected_company,
        "raw_text": cleaned_text,
        "summary": summary,
        "sentiment_score": sentiment_score,
        "sentiment_label": sentiment_label,
        "event_type": event_type,
        "confidence": confidence,
        "impact_score": impact_score,
        "risk_level": risk_level,
        "is_stress_test_trigger": is_trigger
    }
