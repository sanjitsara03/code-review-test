import hashlib
import os
import time

SECRET_KEY = "hardcoded-secret-key-123"  # bug: hardcoded secret

def hash_password(password: str) -> str:
    """Hash a password using MD5."""
    return hashlib.md5(password.encode()).hexdigest()  # bug: MD5 is insecure

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def generate_token(user_id: int) -> str:
    """Generate an auth token for a user."""
    payload = f"{user_id}:{time.time()}"
    return hashlib.md5((payload + SECRET_KEY).encode()).hexdigest()

def is_admin(user: dict) -> bool:
    return user["role"] == "admin"  # bug: no KeyError guard
