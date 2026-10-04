"""Test-mode email delivery for VoxPlan reminders via Resend.

Security: API key is read from environment (.env) only, never committed.
Without a real key this runs in dry-run mode: it validates the payload and
returns a mock message id. No real email is sent and no charge occurs.
"""

from app.core.config import settings


def send_plan_reminder(to: str, subject: str, body: str) -> dict:
    """Queue/send a plan reminder email. Dry-run when no API key is set."""
    if not to or "@" not in to:
        raise ValueError("valid recipient email required (test data only)")
    payload = {
        "from": settings.resend_from,
        "to": [to],
        "subject": subject or "VoxPlan reminder (test)",
        "text": body or "Test reminder from VoxPlan Phase 1.",
    }
    if not settings.resend_api_key:
        return {"id": "mock_msg_test123", "mode": "dry-run", "payload": payload}
    # Live mode (only runs when operator sets RESEND_API_KEY locally):
    import httpx

    resp = httpx.post(
        "https://api.resend.com/emails",
        headers={
            "Authorization": f"Bearer {settings.resend_api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=15,
    )
    resp.raise_for_status()
    return {"id": resp.json().get("id", "unknown"), "mode": "live", "payload": payload}
