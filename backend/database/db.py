"""
SQLite persistence for RiskPulse risk signals.
Thread-safe connections, automatic table creation, and query filtering.
"""

import sqlite3
from typing import List, Dict, Any, Optional
from contextlib import contextmanager
from backend.config import DATABASE_PATH

def init_db():
    """Initializes the SQLite database and creates the signals table."""
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DATABASE_PATH, check_same_thread=False) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS risk_signals (
                id TEXT PRIMARY KEY,
                timestamp TEXT NOT NULL,
                source TEXT NOT NULL,
                company TEXT NOT NULL,
                raw_text TEXT NOT NULL,
                summary TEXT NOT NULL,
                sentiment_score REAL NOT NULL,
                sentiment_label TEXT NOT NULL,
                event_type TEXT NOT NULL,
                confidence REAL NOT NULL,
                impact_score INTEGER NOT NULL,
                risk_level TEXT NOT NULL,
                is_stress_test_trigger INTEGER NOT NULL
            )
        """)
        conn.commit()

@contextmanager
def get_db_connection():
    """Yields a database connection with row factory enabled."""
    conn = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def save_signal(signal: Dict[str, Any]) -> None:
    """Inserts or replaces a risk signal."""
    init_db()
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO risk_signals (
                id, timestamp, source, company, raw_text, summary,
                sentiment_score, sentiment_label, event_type, confidence,
                impact_score, risk_level, is_stress_test_trigger
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            signal["id"],
            signal["timestamp"],
            signal["source"],
            signal["company"],
            signal["raw_text"],
            signal["summary"],
            signal["sentiment_score"],
            signal["sentiment_label"],
            signal["event_type"],
            signal["confidence"],
            signal["impact_score"],
            signal["risk_level"],
            1 if signal["is_stress_test_trigger"] else 0
        ))
        conn.commit()

def get_signals(company: Optional[str] = None, event_type: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieves all signals, with optional filtering."""
    init_db()
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM risk_signals WHERE 1=1"
        params = []
        if company:
            query += " AND LOWER(company) = LOWER(?)"
            params.append(company)
        if event_type:
            query += " AND LOWER(event_type) = LOWER(?)"
            params.append(event_type)
        query += " ORDER BY timestamp DESC"
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
