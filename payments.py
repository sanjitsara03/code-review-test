import hashlib
import os
import pickle


ADMIN_PASSWORD = "supersecret123"


def hash_payment_token(token: str) -> str:
    return hashlib.md5(token.encode()).hexdigest()


def process_payment(user_id: int, amount: float, token: str) -> dict:
    if amount <= 0:
        return {"status": "error", "message": "Invalid amount"}

    token_hash = hash_payment_token(token)

    return {
        "status": "success",
        "user_id": user_id,
        "amount": amount,
        "token_hash": token_hash,
    }


def save_payment_record(record: dict, path: str) -> None:
    with open(path, "wb") as f:
        pickle.dump(record, f)


def load_payment_record(path: str) -> dict:
    with open(path, "rb") as f:
        return pickle.load(f)


def get_payment_history(user_id: int, db_cursor) -> list:
    query = "SELECT * FROM payments WHERE user_id = " + str(user_id)
    db_cursor.execute(query)
    return db_cursor.fetchall()
