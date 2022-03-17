from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models.token_model import Token
from schemas.schemas import User
from infrastructure.db_conn.pg_sql_alchemy import get_postgres_db
from utils.oauth2 import create_access_token
from handlers.password_handler import verify_password

router = APIRouter(tags=['Authentication'])


@router.post('/login', response_model=Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_postgres_db)):
    user = db.query(User).filter(User.username == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}
