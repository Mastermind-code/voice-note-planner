def test_plans_and_tasks_flow(client, auth_headers):
    assert client.get("/plans/").status_code == 401

    plan = client.post(
        "/plans/",
        json={"title": "Week plan", "scope": "week", "source": "manual"},
        headers=auth_headers,
    )
    assert plan.status_code == 201
    plan_id = plan.json()["id"]

    bad_scope = client.post(
        "/plans/", json={"title": "x", "scope": "year"}, headers=auth_headers
    )
    assert bad_scope.status_code == 422

    listed = client.get("/plans/?scope=week", headers=auth_headers).json()
    assert len(listed) == 1
    assert client.get("/plans/?scope=day", headers=auth_headers).json() == []

    task = client.post(
        "/tasks/",
        json={"plan_id": plan_id, "title": "Call mum"},
        headers=auth_headers,
    )
    assert task.status_code == 201
    task_id = task.json()["id"]

    done = client.patch(
        f"/tasks/{task_id}", json={"is_done": True}, headers=auth_headers
    )
    assert done.status_code == 200
    assert done.json()["is_done"] is True

    assert client.get(f"/plans/{plan_id}", headers=auth_headers).status_code == 200
    assert client.delete(f"/tasks/{task_id}", headers=auth_headers).status_code == 204
    assert client.delete(f"/plans/{plan_id}", headers=auth_headers).status_code == 204
    assert client.get("/plans/", headers=auth_headers).json() == []


def test_users_are_isolated(client):
    h1 = _register_and_login(client, "a@example.com")
    h2 = _register_and_login(client, "b@example.com")
    plan_id = client.post("/plans/", json={"title": "A plan"}, headers=h1).json()["id"]
    assert client.get(f"/plans/{plan_id}", headers=h2).status_code == 404


def _register_and_login(client, email):
    client.post("/auth/register", json={"email": email, "password": "secret123"})
    res = client.post("/auth/login", data={"username": email, "password": "secret123"})
    return {"Authorization": f"Bearer {res.json()['access_token']}"}
