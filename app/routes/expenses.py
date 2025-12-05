from fastapi import APIRouter, HTTPException, Depends
from app.database import get_connection
from app.auth import *
from app.models import *

# Додати валідацію!

def amount_to_cents(amount:float) -> int:
    return int(amount * 100)


def сents_to_float(amount_in_cents:int) -> float:
    return amount_in_cents / 100.0

router = APIRouter(tags=['Expenses'])

@router.post("/add") #work
def add_expense(expense: ExpenseCreate, current_user_id: int = Depends(get_current_user), conn = Depends(get_connection)):
    with conn:
        c = conn.cursor()
        amount_in_cents = amount_to_cents(expense.amount)
        c.execute("""INSERT INTO expenses (expense_name, amount, user_id, category_id) VALUES (?, ?, ?, ?)""", (expense.expense_name, amount_in_cents, current_user_id, expense.category_id))
        return {"message": "Expense added"}


@router.post("/get_expenses") #work
def get_expenses(сurrent_user_id: int = Depends(get_current_user), conn = Depends(get_connection)):
    with conn:
        c = conn.cursor()
        c.execute("""SELECT expenses.expense_name, expenses.amount, categories.category FROM expenses 
                  LEFT JOIN categories ON expenses.category_id = categories.id WHERE user_id = ?""", (сurrent_user_id,))
        exp = c.fetchall()
    if not exp:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    result = []
    for name, amount_in_cents, category in exp:
        amount_float = сents_to_float(amount_in_cents) #decimal python ВИНЕСТИ В ФУНКІЮ

        result.append({
                "expense_name": name,
                "amount": amount_float,
                "category": category
            })    
    return result
# Add right Join

    
@router.delete("/delete") #work
def delete_expense(id: int, сurrent_user_id: int = Depends(get_current_user), conn = Depends(get_connection)):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""SELECT * FROM expenses WHERE id = ? """, (id, ))
        exp = c.fetchone() 
        if not exp:
            raise HTTPException(status_code=404, detail="Expense not found")
        c.execute("""DELETE FROM expenses WHERE id = ? AND user_id = ? """, (id, сurrent_user_id))
        return {"detail": "Expense was deleted"}

            
