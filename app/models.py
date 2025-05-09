from pydantic import BaseModel

class Expense(BaseModel): 
    id: int
    name: str
    amount: float
    
class User(BaseModel):
    user_id: int
    user_name: str
