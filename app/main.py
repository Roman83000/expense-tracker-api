from fastapi import FastAPI, status, Depends, HTTPException

from app.routes import users, expenses
from app.database import create_tables
from typing import Annotated
from sqlalchemy.orm import Session
from app.auth import router as auth_router
create_tables()

app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)

app.include_router(auth_router)

#в перспективі зробити авторизацію по кукі чи токєну