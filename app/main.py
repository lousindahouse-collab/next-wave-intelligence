from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models import entities  # noqa: F401
from app.db.migrations import apply_runtime_migrations

Base.metadata.create_all(bind=engine)
apply_runtime_migrations(engine)

app = FastAPI(title=settings.app_name, version="1.3.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/")
def root():
    return {
        "name": "Next Wave V1.3",
        "docs": "/docs",
        "dashboard": "/api/v1/dashboard",
        "live_signals": "/api/v1/live/signals",
        "reddit_status": "/api/v1/reddit/status",
        "reddit_clusters": "/api/v1/reddit/clusters",
    }
