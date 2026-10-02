"""
Loader module for financial news datasets.
Validates required columns, parses timestamps, and cleans text content.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional
import pandas as pd
from datetime import datetime
from backend.config import DATA_DIR
from backend.ingestion.cleaner import clean_financial_text

DEFAULT_NEWS_PATH = DATA_DIR / "news_sample.csv"

def parse_iso_timestamp(timestamp_str: Any) -> datetime:
    """Safely parse multiple timestamp formats."""
    if isinstance(timestamp_str, datetime):
        return timestamp_str
    
    clean_str = str(timestamp_str).strip()
    if clean_str.endswith("Z"):
        clean_str = clean_str[:-1] + "+00:00"
    
    return datetime.fromisoformat(clean_str)

def load_news_data(file_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """
    Loads news dataset from CSV and returns structured, cleaned records.
    """
    path = file_path or DEFAULT_NEWS_PATH
    if not path.exists():
        raise FileNotFoundError(f"News dataset not found at {path}")

    df = pd.read_csv(path)
    required_cols = {"id", "timestamp", "source", "company", "headline", "article_text"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in news CSV: {missing}")

    records = []
    for _, row in df.iterrows():
        headline = clean_financial_text(row["headline"])
        article = clean_financial_text(row["article_text"])
        combined_text = f"{headline}. {article}".strip()

        records.append({
            "id": str(row["id"]),
            "timestamp": parse_iso_timestamp(row["timestamp"]),
            "source": str(row["source"]),
            "company": str(row["company"]),
            "headline": headline,
            "article_text": article,
            "text": combined_text
        })

    return records
