"""
Main entry point for RiskPulse FastAPI application.
Configures CORS middleware, registers routers, and sets up startup ingestion.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.api.routes import router as api_router
from backend.database.db import init_db
from backend.api.routes import run_batch_ingestion

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initializes SQLite database and preloads synthetic demonstration records if empty."""
    init_db()
    try:
        run_batch_ingestion()
    except Exception as exc:
        print(f"Initial ingestion notice: {exc}")
    yield

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.description,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    """Root info endpoint."""
    return {
        "app": settings.app_name,
        "tagline": settings.tagline,
        "version": settings.app_version,
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
