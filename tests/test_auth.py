import pytest
from auth import hash_password, verify_password, generate_token, is_admin


def test_hash_password_returns_string():
    result = hash_password("secret")
    assert isinstance(result, str)
    assert len(result) == 32  # MD5 hex digest length


def test_verify_password_correct():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed) is True


def test_verify_password_wrong():
    hashed = hash_password("mypassword")
    assert verify_password("wrong", hashed) is False


def test_generate_token_returns_string():
    token = generate_token(1)
    assert isinstance(token, str)
    assert len(token) > 0


def test_is_admin_true():
    assert is_admin({"role": "admin"}) is True


def test_is_admin_false():
    assert is_admin({"role": "user"}) is False
