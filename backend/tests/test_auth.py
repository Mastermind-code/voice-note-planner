def test_register_login_me(client):
    res = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secret123"}
    )
    assert res.status_code == 201
    assert res.json()["email"] == "test@example.com"

    dup = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secret123"}
    )
    assert dup.status_code == 400

    login = client.post(
        "/auth/login", data={"username": "test@example.com", "password": "secret123"}
    )
    assert login.status_code == 200
    assert login.json()["token_type"] == "bearer"

    bad = client.post(
        "/auth/login", data={"username": "test@example.com", "password": "wrong"}
    )
    assert bad.status_code == 401

    me = client.get(
        "/auth/me", headers={"Authorization": f"Bearer {login.json()['access_token']}"}
    )
    assert me.status_code == 200
    assert me.json()["email"] == "test@example.com"

    assert client.get("/auth/me").status_code == 401
