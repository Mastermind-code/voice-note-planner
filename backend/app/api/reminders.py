from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.email import send_plan_reminder
from app.services.whatsapp import send_whatsapp_reminder

router = APIRouter()


class ReminderTestIn(BaseModel):
    to: str = "test@example.com"
    subject: str = "VoxPlan reminder (test)"
    body: str = "Call mum tomorrow — test reminder from VoxPlan."


class WhatsAppTestIn(BaseModel):
    to: str = "+15550001111"
    body: str = "VoxPlan test: Call mum tomorrow."


@router.post("/test")
def test_reminder(payload: ReminderTestIn):
    """Trigger a test-mode reminder email (no real send without API key)."""
    try:
        result = send_plan_reminder(payload.to, payload.subject, payload.body)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {"status": "queued (test mode)", **result}


@router.post("/whatsapp/test")
def test_whatsapp_reminder(payload: WhatsAppTestIn):
    """Trigger a test-mode WhatsApp reminder (no real send without token)."""
    try:
        result = send_whatsapp_reminder(payload.to, payload.body)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {"status": "queued (test mode)", **result}
