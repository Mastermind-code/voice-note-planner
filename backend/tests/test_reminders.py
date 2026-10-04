from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_reminder_dry_run():
    response = client.post(
        "/reminders/test",
        json={
            "to": "test@example.com",
            "subject": "VoxPlan reminder (test)",
            "body": "Call mum tomorrow — test reminder.",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "queued (test mode)"
    assert data["mode"] == "dry-run"
    assert data["id"] == "mock_msg_test123"


def test_reminder_rejects_bad_email():
    response = client.post("/reminders/test", json={"to": "not-an-email"})
    assert response.status_code in (400, 422, 500)
