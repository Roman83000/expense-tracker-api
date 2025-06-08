from fastapi import APIRouter, HTTPException
from app.database import get_connection

router = APIRouter(prefix="/users")

def simple_password(password: str) -> str: # змінити неймінг
    hash_val = 0
    for char in password:
        hash_val = (hash_val * 31 + ord(char)) % (2**32)
    return hex(hash_val)
    

def check_auth(email: str, password: str,) -> bool:  # Переробив щоб перевіряв мейл та пароль
    conn = get_connection()
    hashed_pass = simple_password(password)
    with conn:
        c = conn.cursor()
        c.execute("""SELECT * FROM users WHERE email = ? AND password_hash = ? """, (email, hashed_pass))
        final_check = c.fetchone()
        if final_check:
            return True
    return False