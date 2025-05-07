from fastapi import FastAPI, Depends, HTTPException, Response, Query 
from pydantic import BaseModel, Field # imported for making classes
from database import *
import uvicorn # the engine that runs backend application on FastAPI.

app = FastAPI() #create an app

class Expense(BaseModel): 
    id: int
    name: str
    amount: float
    
class User(BaseModel):
    user_id: int
    user_name: str

create_tables() # Create tables by calling a function from the database file
conn = get_connection() 
c = conn.cursor()        

@app.get("/users") # Має працювати
def get_users():
    with conn:
        c.execute("SELECT * FROM users") 
        return c.fetchall() 

@app.get("/users/{user_id}/expenses") # має працювати
def get_expenses(user_id: int):
    with conn:
        c.execute("SELECT * FROM expenses WHERE user_id = :user_id", {'user_id': user_id})
        exp = c.fetchall()

    if not exp:
        raise HTTPException(status_code=404, detail="No expenses found for this user")
    
    return exp


@app.post("/users/{user_name}") # Має працювати
def add_user(user_name: str):
    with conn:
        c.execute("""INSERT INTO users (user_name) VALUES (:user_name)""", {'user_name': user_name})
    
    return {"message": "User added"}




@app.post("/users/{user_id}/expenses/") # має працювати
def add_expense(user_id: int, amount: float, expense_name: str):
    with conn:
        c.execute("""INSERT INTO expenses (expense_name, amount, user_id) VALUES 
                  (:expense_name, :amount, :user_id)""",
                  {'expense_name': expense_name, 'amount': amount, 'user_id': user_id})
        return {"message": "Expense added"}
    
   


@app.delete("/users/{id}") # має працювати. сам додумався як повністю коректно видалити юзера
def delete_user(id: int):
    with conn:
        c.execute("""SELECT * FROM users WHERE id = :id""", {'id': id,})
        user = c.fetchone()
        if user:
            c.execute("""DELETE FROM expenses WHERE user_id = :id""", {'id': id,})
            c.execute("""DELETE FROM users WHERE id = :id""", {'id': id,})
            return {"detail": "User was deleted"}
    raise HTTPException(status_code=404, detail="User not found")
        

@app.delete("/users/{user_id}/expenses/{id}") # сам написав!! тільки на помилки перевірив з джипіті
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


    


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
