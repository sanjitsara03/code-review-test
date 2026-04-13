from session import create_session, get_session, delete_session


def test_create_session_returns_token():
    token = create_session(1)
    assert isinstance(token, str)
    assert len(token) > 0


def test_get_session_returns_data():
    token = create_session(42)
    session = get_session(token)
    assert session["user_id"] == 42


def test_delete_session():
    token = create_session(99)
    delete_session(token)
    # no assertion on missing token behaviour — bug in test
