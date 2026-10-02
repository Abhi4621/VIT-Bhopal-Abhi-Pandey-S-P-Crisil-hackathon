import pytest
from backend.database.db import init_db, save_signal, get_signals
from backend.nlp.risk_engine import analyze_text

def test_database_operations(tmp_path):
    init_db()
    signal = analyze_text("HDFC Bank reports quarterly net profit growth and declining NPA.", company="HDFC Bank", source="Test Feed")
    save_signal(signal)

    all_signals = get_signals()
    assert len(all_signals) >= 1
    found = next((s for s in all_signals if s["id"] == signal["id"]), None)
    assert found is not None
    assert found["company"] == "HDFC Bank"
    assert found["sentiment_label"] == "Positive"

    filtered = get_signals(company="HDFC Bank")
    assert len(filtered) >= 1
    assert all(s["company"].lower() == "hdfc bank" for s in filtered)
