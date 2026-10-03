"""
Pydantic schemas for API requests, responses, and risk signal models.
"""

from typing import Optional, List
from pydantic import BaseModel, Field

class AnalyzeRequest(BaseModel):
    company: Optional[str] = Field(default=None, description="Target company or entity name")
    text: str = Field(..., min_length=3, description="Financial text, article, or social post to analyze")
    source: Optional[str] = Field(default="API Ingestion", description="Source description")

class AnalyzeResponse(BaseModel):
    id: str
    timestamp: str
    company: str
    source: str
    summary: str
    sentiment_score: float = Field(..., ge=-1.0, le=1.0)
    sentiment_label: str
    event_type: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    impact_score: int = Field(..., ge=1, le=10)
    risk_level: str
    is_stress_test_trigger: bool

class HealthResponse(BaseModel):
    status: str
    app: str
    version: str
    database_ready: bool

class StressTestRequest(BaseModel):
    event_type: str = Field(default="Geopolitical", description="Event type for scenario shocks")
    impact_score: int = Field(default=9, ge=1, le=10, description="Prototype impact score (1-10)")
    custom_shocks: Optional[dict] = Field(default=None, description="Optional custom shock overrides by asset class")

class IngestResponse(BaseModel):
    status: str
    news_records_ingested: int
    social_records_ingested: int
    total_signals: int
