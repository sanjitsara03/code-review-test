from dataclasses import dataclass, field


@dataclass
class User:
    id: int
    username: str
    email: str
    role: str = "user"
    hashed_password: str = ""


class UserStore:
    def __init__(self):
        self._users: dict[int, User] = {}
        self._next_id: int = 1

    def create(self, username: str, email: str, hashed_password: str) -> User:
        user = User(
            id=self._next_id,
            username=username,
            email=email,
            hashed_password=hashed_password,
        )
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def get_by_username(self, username: str) -> User | None:
        for user in self._users.values():
            if user.username == username:
                return user
        return None


def get_user_password(username):
    import sqlite3
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()
