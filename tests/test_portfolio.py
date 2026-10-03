import pytest
from backend.portfolio.portfolio import load_portfolio_data, get_portfolio_summary
from backend.portfolio.stress_test import run_stress_test, SCENARIO_SHOCKS

def test_load_portfolio_data():
    assets = load_portfolio_data()
    assert len(assets) >= 8
    first = assets[0]
    assert "asset_id" in first
    assert "asset_type" in first
    assert "value" in first
    assert first["value"] > 0

def test_portfolio_summary():
    summary = get_portfolio_summary()
    assert summary["total_value"] > 0
    assert summary["asset_count"] >= 8
    assert "Equity" in summary["asset_type_allocation"]
    assert "Corporate Bond" in summary["asset_type_allocation"]

def test_stress_test_geopolitical_trigger():
    # Impact score >= 7 triggers shocks
    result = run_stress_test(event_type="Geopolitical", impact_score=9)
    assert result["is_triggered"] is True
    assert result["portfolio_value_before"] > 0
    assert result["portfolio_value_after"] != result["portfolio_value_before"]
    assert result["percentage_change"] < 0  # Net drawdown
    assert len(result["asset_breakdown"]) >= 8

def test_stress_test_low_impact_no_trigger():
    # Impact score < 7 does not trigger shocks
    result = run_stress_test(event_type="Geopolitical", impact_score=5)
    assert result["is_triggered"] is False
    assert result["portfolio_value_after"] == result["portfolio_value_before"]
    assert result["absolute_loss"] == 0.0
    assert result["percentage_change"] == 0.0

def test_stress_test_credit_event():
    result = run_stress_test(event_type="Credit Event", impact_score=8)
    assert result["is_triggered"] is True
    # Corporate bonds and loans suffer sharp drops
    corp_bond = next(a for a in result["asset_breakdown"] if a["asset_type"] == "Corporate Bond")
    assert corp_bond["shock_pct"] == -12.0
