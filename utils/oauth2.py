from jose import JWTError, jwt
from datetime import datetime, timedelta
from models import token_model
from schemas import schemas
from infrastructure.db_conn.pg_sql_alchemy import get_postgres_db
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from settings import get_security_settings
from utils.exceptions import credentials_exception

security_settings = get_security_settings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = security_settings.SECRET_KEY
ALGORITHM = security_settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = security_settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = token_model.TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_postgres_db)):
    token = verify_access_token(token, credentials_exception)
    user = db.query(schemas.User).filter(schemas.User.id == token.user_id).first()
    return user
