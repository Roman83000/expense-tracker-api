from fastapi import APIRouter, HTTPException, Depends
from app.database import get_connection
from app.auth import *
from app.models import UserCreate

router = APIRouter(tags=['Users'])

@router.get("/") # work
def get_users(conn = Depends(get_connection)): #Дописати анотації до кожного ендпоінту
    with conn:
        c = conn.cursor()
        c.execute("""SELECT id, user_name FROM users LIMIT 10""") 

        return c.fetchall()
# ескьюель транзакції !!!

@router.post("/") 
def add_user(user: UserCreate, conn = Depends(get_connection)):
    if not get_user_by_email(user.email):  #fastapi middleware вастапі мідлвеар. винести авторизацію окремо а не в кожен запит
        password_hash = hashed_password(user.password) 
        with conn:
            c = conn.cursor()
            c.execute("""INSERT INTO users (user_name, email, password_hash) VALUES (?, ?, ?)""", 
                      (user.user_name, user.email, password_hash))
        
        return {"message": "User added"}
    raise HTTPException(status_code=401, detail="Unauthorized user") 


@router.delete("/delete_user") #work
def delete_user(current_user_id: int = Depends(get_current_user), conn = Depends(get_connection)):
    with conn: 
        c = conn.cursor()
        c.execute("""DELETE FROM users WHERE id = ? """, (current_user_id,))
        return {"detail": "User was deleted"}
    
