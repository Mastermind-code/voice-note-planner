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
    # POST https://api.resend.com/emails with Authorization: Bearer <key>.
    # Kept uncalled in tests; test suite asserts dry-run path only.
    return {"id": "live_disabled_in_tests", "mode": "live-deferred", "payload": payload}
