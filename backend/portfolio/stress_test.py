"""
Module B — Strategic Portfolio Stress Testing Engine.
Applies scenario shocks to multi-asset portfolios when high-impact risk signals (Impact >= 7) occur.
Calculates before and after valuations, absolute loss, and percentage drawdown.
"""

from typing import Dict, Any, List, Optional
from backend.portfolio.portfolio import load_portfolio_data

# Synthetic scenario shock matrix by asset class (Hackathon illustrative assumptions)
SCENARIO_SHOCKS: Dict[str, Dict[str, float]] = {
    "Geopolitical": {
        "Equity": -0.10,
        "Corporate Bond": -0.05,
        "Government Bond": 0.02,
        "Commodity Exposure": 0.08,
        "Derivative": -0.06,
        "Loan": -0.04
    },
    "Macroeconomic": {
        "Equity": -0.07,
        "Corporate Bond": -0.05,
        "Government Bond": -0.03,
        "Commodity Exposure": -0.02,
        "Derivative": -0.04,
        "Loan": -0.08
    },
    "Credit Event": {
        "Corporate Bond": -0.12,
        "Loan": -0.08,
        "Derivative": -0.05,
        "Equity": -0.08,
        "Government Bond": 0.01,
        "Commodity Exposure": 0.00
    },
    "Regulatory": {
        "Equity": -0.06,
        "Corporate Bond": -0.02,
        "Derivative": -0.03,
        "Loan": -0.02,
        "Government Bond": 0.00,
        "Commodity Exposure": 0.00
    },
    "Default": {
        "Equity": -0.04,
        "Corporate Bond": -0.02,
        "Government Bond": 0.00,
        "Commodity Exposure": 0.00,
        "Derivative": -0.02,
        "Loan": -0.02
    }
}

def run_stress_test(
    event_type: str,
    impact_score: int,
    custom_shocks: Optional[Dict[str, float]] = None,
    assets: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    Executes strategic stress test for a given financial event.
    Enforces impact_score >= 7 trigger logic and calculates net drawdown.
    """
    is_triggered = impact_score >= 7

    current_assets = assets if assets is not None else load_portfolio_data()
    shocks = custom_shocks or SCENARIO_SHOCKS.get(event_type, SCENARIO_SHOCKS["Default"])

    total_before = 0.0
    total_after = 0.0
    asset_breakdown = []

    for asset in current_assets:
        val_before = asset["value"]
        asset_type = asset["asset_type"]

        # Apply specific shock or default 0% if asset type unknown
        shock_pct = shocks.get(asset_type, 0.0) if is_triggered else 0.0
        val_after = max(0.0, val_before * (1.0 + shock_pct))
        change_val = val_after - val_before

        total_before += val_before
        total_after += val_after

        asset_breakdown.append({
            "asset_id": asset["asset_id"],
            "asset_name": asset["asset_name"],
            "asset_type": asset_type,
            "sector": asset.get("sector", "General"),
            "value_before": round(val_before, 2),
            "shock_pct": round(shock_pct * 100, 2),
            "value_after": round(val_after, 2),
            "change_value": round(change_val, 2)
        })

    absolute_loss = total_before - total_after
    percentage_change = ((total_after - total_before) / total_before * 100.0) if total_before > 0 else 0.0

    return {
        "event_type": event_type,
        "impact_score": impact_score,
        "is_triggered": is_triggered,
        "trigger_threshold": 7,
        "scenario_name": f"Synthetic {event_type} Shock Scenario",
        "portfolio_value_before": round(total_before, 2),
        "portfolio_value_after": round(total_after, 2),
        "absolute_loss": round(absolute_loss, 2),
        "percentage_change": round(percentage_change, 2),
        "asset_breakdown": asset_breakdown,
        "disclaimer": "Synthetic hackathon assumptions for demonstration purposes, not real financial forecasts."
    }
