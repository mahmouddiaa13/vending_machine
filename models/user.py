from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime


class Role(str, Enum):
    BUYER = 'buyer'
    SELLER = 'seller'


class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[Role] = "buyer"
    deposit: Optional[str] = 0


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True
