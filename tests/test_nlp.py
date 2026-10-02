import pytest
from backend.nlp.sentiment import extract_sentiment
from backend.nlp.event_classifier import classify_event
from backend.nlp.impact_score import calculate_impact, map_impact_to_level
from backend.nlp.risk_engine import analyze_text, detect_entity

def test_sentiment_positive():
    text = "Tata Motors reports record quarterly net profit growth and strong sales surge."
    result = extract_sentiment(text)
    assert result["sentiment_score"] > 0.0
    assert result["sentiment_label"] == "Positive"
    assert -1.0 <= result["sentiment_score"] <= 1.0

def test_sentiment_negative_and_negation():
    text = "Adani Enterprises faces severe debt default risk and alarming liquidity crisis."
    neg_result = extract_sentiment(text)
    assert neg_result["sentiment_score"] < 0.0
    assert neg_result["sentiment_label"] == "Negative"

    negated_text = "The quarterly numbers are not good."
    negated_result = extract_sentiment(negated_text)
    assert negated_result["sentiment_score"] <= 0.0

def test_sentiment_neutral():
    text = "The committee held a regular procedural meeting on Thursday."
    result = extract_sentiment(text)
    assert result["sentiment_label"] == "Neutral"
    assert -0.2 <= result["sentiment_score"] <= 0.2

def test_event_classification():
    geo = classify_event("Sanctions and military conflict escalate across shipping straits.")
    assert geo["event_type"] == "Geopolitical"
    assert 0.0 <= geo["confidence"] <= 1.0

    credit = classify_event("Rating agency placed debt instruments on credit watch downgrade due to high leverage.")
    assert credit["event_type"] == "Credit Event"

    macro = classify_event("Central bank announces unexpected 50 basis points interest rate hike to tame inflation.")
    assert macro["event_type"] == "Macroeconomic"

    reg = classify_event("Securities regulator initiated formal audit probe over reporting irregularities.")
    assert reg["event_type"] == "Regulatory"

    launch = classify_event("Infosys unveils next-generation enterprise AI orchestration suite.")
    assert launch["event_type"] == "Product Launch"

def test_impact_score_bounds_and_triggers():
    # Severe geopolitical event should trigger stress test (>= 7)
    high_impact = calculate_impact(-0.85, "Geopolitical", "Sanctions and conflict cause severe supply disruption and halt.")
    assert 1 <= high_impact["impact_score"] <= 10
    assert high_impact["impact_score"] >= 7
    assert high_impact["is_stress_test_trigger"] is True
    assert high_impact["risk_level"] in ["High", "Critical"]

    # Mild product launch should have low/moderate impact (< 7)
    low_impact = calculate_impact(0.70, "Product Launch", "Company announces innovative new software feature rollout.")
    assert 1 <= low_impact["impact_score"] <= 10
    assert low_impact["impact_score"] < 7
    assert low_impact["is_stress_test_trigger"] is False
    assert low_impact["risk_level"] in ["Low", "Moderate"]

def test_entity_detection():
    assert detect_entity("Breaking report on reliance industries oil refinery") == "Reliance Industries"
    assert detect_entity("Tata Motors inaugurates new EV plant") == "Tata Motors"
    assert detect_entity("Market updates for general trading") == "General Market"

def test_unified_risk_engine():
    text = "Tata Motors faces supply chain disruption and halt amid regional conflict."
    signal = analyze_text(text, company="Tata Motors", source="Test News Wire")
    assert signal["company"] == "Tata Motors"
    assert signal["sentiment_label"] == "Negative"
    assert signal["event_type"] == "Geopolitical"
    assert signal["impact_score"] >= 7
    assert signal["is_stress_test_trigger"] is True
    assert signal["summary"] != ""
