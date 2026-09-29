import pytest
from app.core.security import hash_password, verify_password, create_access_token, decode_access_token

def test_password_hashing():
    raw = "SecurePassword123!"
    hashed = hash_password(raw)
    assert hashed != raw
    assert verify_password(raw, hashed) is True
    assert verify_password("WrongPassword", hashed) is False

def test_jwt_tokens():
    user_id = "test-user-uuid-1234"
    token = create_access_token(user_id)
    assert token is not None
    decoded_id = decode_access_token(token)
    assert decoded_id == user_id
