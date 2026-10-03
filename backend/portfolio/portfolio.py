"""
Portfolio management module for RiskPulse.
Loads synthetic portfolio assets and computes allocations and exposures.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd
from backend.config import DATA_DIR

DEFAULT_PORTFOLIO_PATH = DATA_DIR / "portfolio.csv"

def load_portfolio_data(file_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Loads synthetic portfolio assets from CSV."""
    path = file_path or DEFAULT_PORTFOLIO_PATH
    if not path.exists():
        raise FileNotFoundError(f"Portfolio file not found at {path}")

    df = pd.read_csv(path)
    required_cols = {"asset_id", "asset_name", "asset_type", "sector", "value", "duration", "credit_risk"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in portfolio CSV: {missing}")

    records = []
    for _, row in df.iterrows():
        records.append({
            "asset_id": str(row["asset_id"]),
            "asset_name": str(row["asset_name"]),
            "asset_type": str(row["asset_type"]),
            "sector": str(row["sector"]),
            "value": float(row["value"]),
            "duration": float(row["duration"]),
            "credit_risk": str(row["credit_risk"])
        })
    return records

def get_portfolio_summary(file_path: Optional[Path] = None) -> Dict[str, Any]:
    """Computes baseline aggregate metrics and allocations for the portfolio."""
    assets = load_portfolio_data(file_path)
    total_value = sum(a["value"] for a in assets)

    # Allocations by asset type
    asset_types: Dict[str, float] = {}
    for a in assets:
        t = a["asset_type"]
        asset_types[t] = asset_types.get(t, 0.0) + a["value"]

    # Allocations by sector
    sectors: Dict[str, float] = {}
    for a in assets:
        s = a["sector"]
        sectors[s] = sectors.get(s, 0.0) + a["value"]

    # Weighted average duration for fixed-income assets
    fixed_income_value = sum(a["value"] for a in assets if a["duration"] > 0)
    if fixed_income_value > 0:
        weighted_duration = sum(a["value"] * a["duration"] for a in assets if a["duration"] > 0) / fixed_income_value
    else:
        weighted_duration = 0.0

    return {
        "total_value": round(total_value, 2),
        "asset_count": len(assets),
        "weighted_duration": round(weighted_duration, 2),
        "asset_type_allocation": {k: round(v, 2) for k, v in asset_types.items()},
        "sector_allocation": {k: round(v, 2) for k, v in sectors.items()},
        "assets": assets
    }
