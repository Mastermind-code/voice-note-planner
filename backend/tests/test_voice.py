def test_voice_ingest_creates_plan_and_tasks(client, auth_headers):
    res = client.post(
        "/voice/ingest",
        files={"file": ("note.ogg", b"fake-bytes", "audio/ogg")},
        data={"transcript": "call mum, finish slides and gym"},
        headers=auth_headers,
    )
    assert res.status_code == 201
    body = res.json()
    assert body["tasks_created"] == 3

    plan = client.get(f"/plans/{body['plan_id']}", headers=auth_headers)
    assert plan.status_code == 200
    assert plan.json()["source"] == "voice"

    tasks = client.get(
        f"/tasks/?plan_id={body['plan_id']}", headers=auth_headers
    ).json()
    assert len(tasks) == 3
    assert all(t["source"] == "voice" for t in tasks)
