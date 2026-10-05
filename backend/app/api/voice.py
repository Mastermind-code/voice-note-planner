"""Voice ingest — persists a voice-sourced plan + tasks (mock AI for now).

Real speech-to-text + LLM extraction land in Phase 3; this endpoint already
stores the plan so mobile/web clients can sync against it.
"""

import re

from fastapi import APIRouter, Depends, Form, UploadFile
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.deps import get_current_user
from app.models.plan import Plan, Task
from app.models.user import User

router = APIRouter()


def mock_extract_tasks(transcript: str) -> list[str]:
    """Placeholder for Phase 3 LLM extraction: split transcript into items."""
    parts = re.split(r",|;|\band\b", transcript)
    return [p.strip().capitalize() for p in parts if p.strip()][:10]


@router.post("/ingest", status_code=201)
async def ingest_voice_note(
    file: UploadFile,
    transcript: str = Form(default=""),
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    plan = Plan(
        user_id=user.id,
        title=f"Voice plan: {file.filename}",
        scope="week",
        source="voice",
        transcript=transcript or None,
    )
    db.add(plan)
    db.flush()
    titles = mock_extract_tasks(transcript) if transcript else []
    for title in titles:
        db.add(Task(user_id=user.id, plan_id=plan.id, title=title, source="voice"))
    db.commit()
    return {
        "plan_id": plan.id,
        "tasks_created": len(titles),
        "note": "mock extraction — real STT + LLM in Phase 3",
    }
