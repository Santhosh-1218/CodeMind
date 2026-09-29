import pytest
import uuid
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_unauthenticated_access_denied():
    res = client.get("/api/auth/me")
    assert res.status_code == 401
    assert "detail" in res.json()

def test_register_and_login_flow():
    uid = str(uuid.uuid4())[:8]
    email = f"testuser_{uid}@codemind.dev"
    password = "TestPassword123!"
    full_name = "Test Developer"

    # 1. Register
    reg_res = client.post("/api/auth/register", json={
        "email": email,
        "password": password,
        "full_name": full_name
    })
    assert reg_res.status_code == 200
    data = reg_res.json()
    assert "token" in data
    assert data["user"]["email"] == email
    cookie = reg_res.cookies.get("codemind_session")
    assert cookie is not None

    # 2. Get /me with cookie
    me_res = client.get("/api/auth/me", cookies={"codemind_session": cookie})
    assert me_res.status_code == 200
    assert me_res.json()["email"] == email

    # 3. Login
    login_res = client.post("/api/auth/login", json={
        "email": email,
        "password": password
    })
    assert login_res.status_code == 200
    new_cookie = login_res.cookies.get("codemind_session")
    assert new_cookie is not None

    # 4. Logout
    logout_res = client.post("/api/auth/logout", cookies={"codemind_session": new_cookie})
    assert logout_res.status_code == 200

    # 5. Access after logout
    post_logout_me = client.get("/api/auth/me", cookies={"codemind_session": new_cookie})
    assert post_logout_me.status_code == 401
