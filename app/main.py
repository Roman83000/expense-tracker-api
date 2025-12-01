from fastapi import FastAPI, status, Depends, HTTPException
from app.routes import users, expenses
from typing import Annotated
from sqlalchemy.orm import Session
from app.auth import router as auth_router


app = FastAPI()

app.include_router(users.router)
app.include_router(expenses.router)

app.include_router(auth_router)

# Авторизація злітає кожен раз коли перезавантаєую сторінку

#в перспективі зробити авторизацію по кукі чи токєну