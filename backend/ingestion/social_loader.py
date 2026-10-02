"""
Loader module for financial social commentary datasets.
Handles social commentary records, null checks, and text cleaning.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd
from datetime import datetime
from backend.config import DATA_DIR
from backend.ingestion.cleaner import clean_financial_text

DEFAULT_SOCIAL_PATH = DATA_DIR / "social_sample.csv"

def parse_iso_timestamp(timestamp_str: Any) -> datetime:
    """Safely parse multiple timestamp formats."""
    if isinstance(timestamp_str, datetime):
        return timestamp_str
    
    clean_str = str(timestamp_str).strip()
    if clean_str.endswith("Z"):
        clean_str = clean_str[:-1] + "+00:00"
    
    return datetime.fromisoformat(clean_str)

def load_social_data(file_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """
    Loads social commentary dataset from CSV and returns structured, cleaned records.
    """
    path = file_path or DEFAULT_SOCIAL_PATH
    if not path.exists():
        raise FileNotFoundError(f"Social dataset not found at {path}")

    df = pd.read_csv(path)
    required_cols = {"id", "timestamp", "source", "company", "text"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in social CSV: {missing}")

    records = []
    for _, row in df.iterrows():
        # Handle potential null or non-string values safely
        raw_text = row["text"] if pd.notna(row["text"]) else ""
        cleaned = clean_financial_text(raw_text)

        records.append({
            "id": str(row["id"]),
            "timestamp": parse_iso_timestamp(row["timestamp"]),
            "source": str(row["source"]),
            "company": str(row["company"]),
            "headline": "",
            "article_text": "",
            "text": cleaned
        })

    return records
