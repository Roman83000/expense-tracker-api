from fastapi import APIRouter
from app.database import get_connection

router = APIRouter(prefix="/users")
conn = get_connection()
c = conn.cursor()

@router.get("/") 
def get_users():
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users") 
        return c.fetchall() 

@router.post("/users/{user_name}") 
def add_user(user_name: str):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""INSERT INTO users (user_name) VALUES (:user_name)""", {'user_name': user_name})
    
    return {"message": "User added"}
