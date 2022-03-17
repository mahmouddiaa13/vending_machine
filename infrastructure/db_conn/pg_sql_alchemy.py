from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from settings import PostgresDBSettings, get_postgres_db_settings
from urllib.parse import quote

db_settings: PostgresDBSettings = get_postgres_db_settings()


def get_db_url(user_name, host, db_port, db_name):
    url = f'postgresql://{user_name}:%s@{host}:{db_port}/{db_name}'
    return url


db_url = get_db_url(db_settings.USER_NAME, db_settings.HOST, 5432, db_settings.NAME)
engine = create_engine(db_url % quote(db_settings.PWD))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_postgres_db():
    db: Session = SessionLocal()
    return db
