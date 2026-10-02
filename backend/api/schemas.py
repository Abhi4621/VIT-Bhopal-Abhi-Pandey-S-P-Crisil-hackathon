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
