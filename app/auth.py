from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.database import get_connection
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.models import Token
import bcrypt
import os
# погуглити які проблеми вирішує кукі та дживіті, та сесії в автентифікації.
# чому у деяких баз даних є окремий процес(сервер) а у деяких ні, в чому різниця різних субд, чому вони існують(йти хронологічно), джойни
# Додати фільтри для витягування витрат, щоб у витрат було більше полів(категорії), щоб можна було додавати різні товари в різні категорії, теги, видаляти
# це зробити ендпоінтами
router = APIRouter(tags=["Auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"
SECRET_KEY = os.getenv("SECRET_KEY", "Zalupa")

def get_user_by_email(email: str):
    conn = get_connection()
    with conn:
        c = conn.cursor()
        c.execute("""SELECT id, user_name, email, password_hash FROM users WHERE email = ?""", (email,))
        row = c.fetchone()
        if row:
            return{
                "id": row[0],
                "user_name": row[1],
                "email": row[2],
                "hashed_password": row[3]
                }
        return None
    
@router.post("/token", response_model=Token)
def login(form_data:OAuth2PasswordRequestForm=Depends()): 
    user = get_user_by_email(form_data.username)
    if not user or not check_auth(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    token_data = {"sub": str(user["id"])}
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    token_data["exp"] = expire
    
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token":token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return int(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail= "Invalid token")



def check_auth(email: str, password: str,) -> bool:  
    user = get_user_by_email(email)
    if not user:
        return False
    return verify_password(password, user["hashed_password"])

def hashed_password(password: str) -> str: 
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")
    

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8")) #сіль генерується автоматично






























# def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: str = payload.get("sub")
#         if user_id is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return int(user_id)
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Could not validate token")



    





























