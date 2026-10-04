"""
Application configuration for RiskPulse.
Handles base paths, data locations, and database configuration.
"""

import os
import tempfile
from pathlib import Path
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# On Vercel / AWS Lambda, use writable /tmp directory
if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
    DATABASE_PATH = Path(tempfile.gettempdir()) / "riskpulse.db"
else:
    DATABASE_PATH = BASE_DIR / "backend" / "database" / "riskpulse.db"

class Settings(BaseModel):
    app_name: str = "RiskPulse"
    app_version: str = "1.0.0"
    description: str = "AI/NLP Financial Risk Intelligence Platform"
    tagline: str = "Turning financial noise into actionable risk signals."
    stress_test_threshold: int = Field(default=7, ge=1, le=10, description="Impact score threshold (1-10) to trigger stress testing")
    database_url: str = f"sqlite:///{DATABASE_PATH}"
    debug: bool = False

# Ensure required runtime directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

settings = Settings()
