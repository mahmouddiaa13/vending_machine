from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from infrastructure.db_conn.pg_sql_alchemy import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="buyer")
    deposit = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('now()'))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    product_name = Column(String, nullable=False, unique=True)
    cost = Column(Integer, nullable=False)
    amount_available = Column(Integer, nullable=False, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('now()'))
    seller_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=0)

    seller = relationship("User")
