from fastapi import FastAPI

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, plans, reminders, tasks, voice
from app.core.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="VoxPlan API", version="0.1.0", lifespan=lifespan)

# Dev-open CORS so the local static prototype (file:// or :8000) can call
# the API. Tighten allow_origins to the real frontend domain in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(reminders.router, prefix="/reminders", tags=["reminders"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
