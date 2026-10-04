from fastapi import FastAPI

from app.api import plans, reminders, tasks, voice

app = FastAPI(title="VoxPlan API", version="0.1.0")

app.include_router(plans.router, prefix="/plans", tags=["plans"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(reminders.router, prefix="/reminders", tags=["reminders"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
