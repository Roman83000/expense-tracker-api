from fastapi import APIRouter, HTTPException, Depends
from app.database import get_connection
from app.auth import *



router = APIRouter(tags=['Expenses'])

@router.post("/add") #work
def add_expense(amount: float, expense_name: str, current_user_id: int = Depends(get_current_user)):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""INSERT INTO expenses (expense_name, amount, user_id) VALUES (?, ?, ?)""", (expense_name, amount, current_user_id))
        return {"message": "Expense added"}


@router.post("/get_expenses") #work
def get_expenses(сurrent_user_id: int = Depends(get_current_user)):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""SELECT * FROM expenses WHERE user_id = ?""", (сurrent_user_id,))
        exp = c.fetchall()
    if not exp:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    return exp


    
@router.delete("/delete") #work
def delete_expense(id: int, сurrent_user_id: int = Depends(get_current_user)):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""SELECT * FROM expenses WHERE id = ? """, (id, ))
        exp = c.fetchone() 
        if not exp:
            raise HTTPException(status_code=404, detail="Expense not found")
        c.execute("""DELETE FROM expenses WHERE id = ? AND user_id = ? """, (id, сurrent_user_id))
        return {"detail": "Expense was deleted"}

            
