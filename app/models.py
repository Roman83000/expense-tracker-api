from pydantic import BaseModel, EmailStr

class Expense(BaseModel): 
    id: int
    name: str
    amount: float
    
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