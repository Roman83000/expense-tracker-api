from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.auth import check_auth, simple_password
from app.models import UserCreate, UserAuth

router = APIRouter(prefix="/users", tags=['Users'])

@router.get("/") # FastApi dependency 
def get_users(): #Дописати анотації до кожного ендпоінту
    conn = get_connection() # має бути в параметрі
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM users") # має бути лімітована кількість юзерів, яка вертається
        return c.fetchall() # повертати список моделей User

# ескьюель транзакції !!!

@router.post("/") 
def add_user(user: UserCreate):
    conn = get_connection() 
    if not check_auth(user.email, user.password):  #fastapi middleware вастапі мідлвеар. винести авторизацію окремо а не в кожен запит
        password_hash = simple_password(user.password) 
        with conn:
            c = conn.cursor()
            c.execute("""INSERT INTO users (user_name, email, password_hash) VALUES (?, ?, ?)""", 
                      (user.user_name, user.email, password_hash))
        
        return {"message": "User added"}
    return {"message": "Try another login or password"} # має вертати помилку (статускод)


@router.delete("/delete") 
def delete_user(user: UserAuth):
    conn = get_connection()
    if check_auth(user.email, user.password):
        password_hash = simple_password(user.password)
        with conn: # 
            c = conn.cursor()
            c.execute("""SELECT id FROM users WHERE email = ? AND password_hash = ? """, (user.email, password_hash))
            temp_id = c.fetchone() # назвати юзер айді
            c.execute("""DELETE FROM expenses WHERE user_id = ? """, (temp_id[0],))
            c.execute("""DELETE FROM users WHERE email = ? AND password_hash = ? """, (user.email, password_hash))
            return {"detail": "User was deleted"}
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Try another login or password"} # має вертати помилку (статускод)
            
