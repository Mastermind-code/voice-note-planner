from fastapi import FastAPI

from app.api import plans, tasks, voice

app = FastAPI(title="Voice Note Planner API", version="0.1.0")

app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(voice.router, prefix="/voice", tags=["voice"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
