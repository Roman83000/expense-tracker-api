from fastapi import APIRouter, HTTPException
from app.database import get_connection

router = APIRouter(prefix="/users")
conn = get_connection()
c = conn.cursor()

@router.get("/{user_id}/expenses")
def get_expenses(user_id: int):
    with conn:
        c.execute("SELECT * FROM expenses WHERE user_id = :user_id", {'user_id': user_id})
        exp = c.fetchall()

    if not exp:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    
    return exp

@router.post("/{user_id}/expenses/")
def add_expense(user_id: int, amount: float, expense_name: str):
    with conn:
        c.execute("""INSERT INTO expenses (expense_name, amount, user_id) VALUES 
                  (:expense_name, :amount, :user_id)""",
                  {'expense_name': expense_name, 'amount': amount, 'user_id': user_id})
        return {"message": "Expense added"}
    
@router.delete("/users/{user_id}/expenses/{id}")
def delete_expense(user_id: int, id: int):
    with conn:
        c.execute("""SELECT * FROM users WHERE id = :user_id""", {'user_id': user_id,})
        user = c.fetchone()
        c.execute("""SELECT * FROM expenses WHERE id = :id""", {'id': id,})
        exp = c.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not exp:
            raise HTTPException(status_code=404, detail="Expense not found")
        if user and exp:
            c.execute("""DELETE FROM expenses WHERE id = :id AND user_id = :user_id""", {'id': id, 'user_id': user_id})
            return {"detail": "Expense was deleted"}
        
    # with conn:
    #     c.execute("""DELETE FROM expenses WHERE id = :id AND user_id = :user_id""",
    #               {'id': id, 'user_id': user_id})
    #     if c.rowcount == 0:
    #         raise HTTPException(status_code=404, detail="Expense not found or does not belong to this user")
    #     return {"detail": "Expense was deleted"}