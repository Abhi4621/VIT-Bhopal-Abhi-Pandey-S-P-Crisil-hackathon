"""
FastAPI routing and endpoint controllers for RiskPulse.
Exposes REST endpoints for analysis, signals query, ingestion, portfolio, and stress tests.
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.config import settings
from backend.api.schemas import (
    AnalyzeRequest, AnalyzeResponse, HealthResponse,
    StressTestRequest, IngestResponse
)
from backend.nlp.risk_engine import analyze_text
from backend.database.db import save_signal, get_signals
from backend.ingestion.news_loader import load_news_data
from backend.ingestion.social_loader import load_social_data
from backend.portfolio.portfolio import get_portfolio_summary
from backend.portfolio.stress_test import run_stress_test

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
def health_check():
    """Health check verifying API and settings status."""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "database_ready": True
    }

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_endpoint(request: AnalyzeRequest):
    """
    Ingests text, runs the complete NLP Risk Engine pipeline,
    persists the resulting structured risk signal to SQLite, and returns it.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")

    signal = analyze_text(
        text=request.text,
        company=request.company,
        source=request.source or "API Ingestion"
    )

    save_signal(signal)
    return signal

@router.get("/signals")
def get_signals_endpoint(
    company: Optional[str] = Query(None, description="Filter signals by company"),
    event_type: Optional[str] = Query(None, description="Filter signals by event type"),
    min_impact: Optional[int] = Query(None, ge=1, le=10, description="Minimum impact score"),
    limit: int = Query(50, ge=1, le=200, description="Max records to return")
):
    """Retrieves stored risk signals with optional filtering."""
    signals = get_signals(company=company, event_type=event_type)
    if min_impact:
        signals = [s for s in signals if s["impact_score"] >= min_impact]
    return signals[:limit]

@router.get("/signals/{company}")
def get_company_signals_endpoint(company: str):
    """Retrieves risk signals for a specific company entity."""
    signals = get_signals(company=company)
    if not signals:
        raise HTTPException(status_code=404, detail=f"No risk signals found for company: {company}")
    return signals

from backend.ingestion.rss_loader import fetch_live_rss_records

@router.post("/ingest", response_model=IngestResponse)
def run_batch_ingestion(include_live: bool = Query(False, description="Optionally ingest live public financial RSS feed")):
    """
    Loads synthetic news and social datasets, processes them through the NLP risk engine,
    and stores all signals in the database. Optionally fetches live public RSS items.
    """
    news_records = load_news_data()
    social_records = load_social_data()
    live_count = 0

    for item in news_records:
        sig = analyze_text(text=item["text"], company=item["company"], source=item["source"])
        save_signal(sig)

    for item in social_records:
        sig = analyze_text(text=item["text"], company=item["company"], source=item["source"])
        save_signal(sig)

    if include_live:
        live_records = fetch_live_rss_records(max_items=5)
        for item in live_records:
            sig = analyze_text(text=item["text"], company=item.get("company"), source=item["source"])
            save_signal(sig)
        live_count = len(live_records)

    all_signals = get_signals()

    return {
        "status": "success",
        "news_records_ingested": len(news_records),
        "social_records_ingested": len(social_records),
        "live_records_ingested": live_count,
        "total_signals": len(all_signals)
    }

@router.post("/ingest/live", response_model=IngestResponse)
def run_live_ingestion():
    """
    Ingests live headlines from free public financial RSS feed and propagates into risk engine.
    Gracefully handles offline environments.
    """
    live_records = fetch_live_rss_records(max_items=10)
    for item in live_records:
        sig = analyze_text(text=item["text"], company=item.get("company"), source=item["source"])
        save_signal(sig)

    all_signals = get_signals()
    return {
        "status": "success",
        "news_records_ingested": 0,
        "social_records_ingested": 0,
        "live_records_ingested": len(live_records),
        "total_signals": len(all_signals)
    }

@router.get("/portfolio")
def get_portfolio_endpoint():
    """Returns baseline synthetic portfolio allocations and asset positions."""
    return get_portfolio_summary()

@router.post("/stress-test")
def run_stress_test_endpoint(request: StressTestRequest):
    """
    Executes Module B Strategic Portfolio Stress Test simulation.
    Shocks portfolio assets if impact_score >= 7.
    """
    return run_stress_test(
        event_type=request.event_type,
        impact_score=request.impact_score,
        custom_shocks=request.custom_shocks
    )
