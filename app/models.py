from pydantic import BaseModel, EmailStr

class ExpenseCreate(BaseModel):
    expense_name: str
    amount: float
    category_id: int|None = None

class Expense(BaseModel): 
    id: int
    name: str
    amount: float
    category_name: str
    
class User(BaseModel):
    user_id: int
    user_name: str

class UserCreate(BaseModel):
    user_name: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str