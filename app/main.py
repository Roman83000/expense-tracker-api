from fastapi import FastAPI
from app.routes import users, expenses
from app.database import create_tables  
create_tables()

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)

#в перспективі зробити авторизацію по кукі чи токєну