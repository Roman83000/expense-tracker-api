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

class UserAuth(BaseModel):
    email: EmailStr
    password: str