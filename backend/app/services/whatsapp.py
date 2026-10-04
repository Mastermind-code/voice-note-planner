"""Test-mode WhatsApp reminders for VoxPlan via WhatsApp Business Cloud API.

Security: token is read from environment (.env) only, never committed.
Without a real token this runs in dry-run mode: it validates the payload and
returns a mock message id. No real message is sent and no charge occurs.
"""

from app.core.config import settings


def send_whatsapp_reminder(to: str, body: str) -> dict:
    """Queue/send a WhatsApp reminder. Dry-run when no token is set."""
    digits = "".join(ch for ch in (to or "") if ch.isdigit())
    if len(digits) < 7:
        raise ValueError("valid recipient phone required (test data only)")
    payload = {
        "messaging_product": "whatsapp",
        "to": digits,
        "type": "text",
        "text": {"body": body or "Test reminder from VoxPlan."},
    }
    if not settings.whatsapp_token:
        return {"id": "mock_whatsapp_test456", "mode": "dry-run", "payload": payload}
    # Live mode (only runs when operator sets WHATSAPP_TOKEN locally):
    # POST https://graph.facebook.com/v21.0/{phone-number-id}/messages
    # with Authorization: Bearer <token>. Kept uncalled in tests.
    return {"id": "live_disabled_in_tests", "mode": "live-deferred", "payload": payload}
