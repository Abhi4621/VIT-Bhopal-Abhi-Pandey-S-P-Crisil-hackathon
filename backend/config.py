"""
Application configuration for RiskPulse.
Handles base paths, data locations, and database configuration.
"""

from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = BASE_DIR / "backend" / "database" / "riskpulse.db"

class Settings(BaseModel):
    app_name: str = "RiskPulse"
    app_version: str = "1.0.0"
    description: str = "AI/NLP Financial Risk Intelligence Platform"
    tagline: str = "Turning financial noise into actionable risk signals."
    stress_test_threshold: int = 7
    database_url: str = f"sqlite:///{DATABASE_PATH}"
    debug: bool = False

settings = Settings()
