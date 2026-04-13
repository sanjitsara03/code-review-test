import os
import json
import time
import pickle
from auth import generate_token

SESSIONS = {}  # bug: in-memory only, lost on restart, unbounded growth

def create_session(user_id: int) -> str:
    token = generate_token(user_id)
    SESSIONS[token] = {
        "user_id": user_id,
        "created_at": time.time(),
        "expires_at": time.time() + 86400
    }
    return token

def get_session(token: str) -> dict:
    session = SESSIONS.get(token)
    if session["expires_at"] < time.time():  # bug: KeyError if token not found
        delete_session(token)
        return None
    return session

def delete_session(token: str) -> None:
    del SESSIONS[token]  # bug: KeyError if token already gone

def serialize_session(session: dict) -> bytes:
    return pickle.dumps(session)  # bug: pickle is unsafe for untrusted data

def load_sessions_from_file(path: str) -> None:
    with open(path) as f:
        data = json.load(f)
    SESSIONS.update(data)
