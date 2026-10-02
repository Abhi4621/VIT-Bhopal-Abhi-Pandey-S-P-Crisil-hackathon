import pytest
from backend.ingestion.cleaner import clean_financial_text
from backend.ingestion.news_loader import load_news_data
from backend.ingestion.social_loader import load_social_data

def test_clean_financial_text():
    raw = "Breaking: Tata Motors &amp; EV battery supply disrupted! Check https://example.com/news   for info."
    cleaned = clean_financial_text(raw)
    assert "&" in cleaned and "&amp;" not in cleaned
    assert "https://" not in cleaned
    assert "  " not in cleaned

def test_clean_financial_text_none_and_empty():
    assert clean_financial_text(None) == ""
    assert clean_financial_text("") == ""

def test_load_news_data():
    news = load_news_data()
    assert len(news) >= 10
    first = news[0]
    assert "company" in first
    assert "headline" in first
    assert "text" in first
    assert first["timestamp"] is not None

def test_load_social_data():
    social = load_social_data()
    assert len(social) >= 8
    first = social[0]
    assert "company" in first
    assert "text" in first
    assert len(first["text"]) > 5
