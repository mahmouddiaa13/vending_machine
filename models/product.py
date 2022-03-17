from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    product_name: str
    amount_available: int
    cost: int
    seller_id: str
