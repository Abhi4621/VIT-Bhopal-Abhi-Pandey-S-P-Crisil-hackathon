import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app"] == "RiskPulse"

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "tagline" in response.json()

def test_analyze_endpoint():
    payload = {
        "company": "Tata Motors",
        "text": "Tata Motors announced severe factory halts due to geopolitical sanctions."
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["company"] == "Tata Motors"
    assert data["sentiment_label"] == "Negative"
    assert data["event_type"] == "Geopolitical"
    assert data["impact_score"] >= 7
    assert data["is_stress_test_trigger"] is True

def test_analyze_empty_text():
    response = client.post("/analyze", json={"company": "Test", "text": "   "})
    assert response.status_code in [400, 422]

def test_get_signals():
    response = client.get("/signals")
    assert response.status_code == 200
    signals = response.json()
    assert isinstance(signals, list)
    assert len(signals) >= 1

def test_get_portfolio():
    response = client.get("/portfolio")
    assert response.status_code == 200
    data = response.json()
    assert "total_value" in data
    assert "asset_type_allocation" in data
    assert data["asset_count"] >= 8

def test_stress_test_endpoint():
    payload = {
        "event_type": "Geopolitical",
        "impact_score": 9
    }
    response = client.post("/stress-test", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["is_triggered"] is True
    assert data["portfolio_value_before"] > data["portfolio_value_after"]
    assert data["percentage_change"] < 0
