from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import UserAuth
from app.auth import check_auth, simple_password

router = APIRouter(prefix="/expenses", tags=['Expenses'])

@router.post("/add")
def add_expense(amount: float, expense_name: str, user: UserAuth):
    conn = get_connection()
    if check_auth(user.email, user.password):
        password_hash = simple_password(user.password)
        with conn:
            c = conn.cursor()
            c.execute("""SELECT id FROM users WHERE email = ? AND password_hash = ? """, (user.email, password_hash))
            temp_id = c.fetchone()
            c.execute("""INSERT INTO expenses (expense_name, amount, user_id) VALUES (?, ?, ?)""", (expense_name, amount, temp_id[0]))
            return {"message": "Expense added"}
    return {"message": "Try another login or password"}

@router.post("/get_expenses") # тут була TypeError: Failed to execute 'fetch' on 'Window': Request with GET/HEAD method cannot have body. Замінив get на post
def get_expenses(user: UserAuth):
    conn = get_connection()
    if check_auth(user.email, user.password):
        password_hash = simple_password(user.password)
        with conn:
            c = conn.cursor()
            c.execute("""SELECT id FROM users WHERE email = ? AND password_hash = ? """, (user.email, password_hash))
            temp_id = c.fetchone()
            c.execute("""SELECT * FROM expenses WHERE user_id = :user_id""", {'user_id': temp_id[0]})
            exp = c.fetchall()
        if not exp:
            raise HTTPException(status_code=404, detail="No expenses found for this user")
        return exp
    return {"message": "Try another login or password"}

    
@router.delete("/delete/{id}")
def delete_expense(id: str, user: UserAuth):
    conn = get_connection()
    if check_auth(user.email, user.password):
        password_hash = simple_password(user.password)
        with conn:
            c = conn.cursor()
            c.execute("""SELECT id FROM users WHERE email = ? AND password_hash = ? """, (user.email, password_hash))
            temp_id = c.fetchone()
            c.execute("""SELECT * FROM users WHERE id = ? """, (temp_id[0],))
            user = c.fetchone()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            c.execute("""SELECT * FROM expenses WHERE id = ? """, (id, ))
            exp = c.fetchone() 
            if not exp:
                raise HTTPException(status_code=404, detail="Expense not found")
            if user and exp:
                c.execute("""DELETE FROM expenses WHERE id = ? AND user_id = ? """, (id, temp_id[0]))
                return {"detail": "Expense was deleted"}
    return {"message": "Try another login or password"}
            
    # with conn:
    #     c.execute("""DELETE FROM expenses WHERE id = :id AND user_id = :user_id""",
    #               {'id': id, 'user_id': user_id})
    #     if c.rowcount == 0:
    #         raise HTTPException(status_code=404, detail="Expense not found or does not belong to this user")
    #     return {"detail": "Expense was deleted"}