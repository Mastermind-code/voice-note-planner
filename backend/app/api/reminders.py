from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.email import send_plan_reminder

router = APIRouter()


class ReminderTestIn(BaseModel):
    to: str = "test@example.com"
    subject: str = "VoxPlan reminder (test)"
    body: str = "Call mum tomorrow — test reminder from VoxPlan."


@router.post("/test")
def test_reminder(payload: ReminderTestIn):
    """Trigger a test-mode reminder email (no real send without API key)."""
    try:
        result = send_plan_reminder(payload.to, payload.subject, payload.body)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {"status": "queued (test mode)", **result}
