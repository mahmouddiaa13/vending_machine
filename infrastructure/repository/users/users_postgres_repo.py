from infrastructure.db_conn.pg_sql_alchemy import get_postgres_db
from infrastructure.repository.users.users_base_repo import UsersBaseRepo
from models.user import UserCreate, UserUpdate
from schemas import schemas


class UsersPostgresRepo(UsersBaseRepo):
    def __init__(self):
        self.db = get_postgres_db()

    async def create_user(self, user: UserCreate):
        new_user = schemas.User(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    async def get_user(self, user_id: int) -> UserCreate:
        user = self.db.query(schemas.User).filter(schemas.User.id == user_id).first()
        return user

    async def update_user(self, user_id: int, updated_user: UserCreate):
        self.db.query(schemas.User).filter(schemas.User.id == user_id).update({"username": updated_user.username},
                                                                              synchronize_session=False)
        self.db.commit()

    async def delete_user(self, user_id: int):
        self.db.query(schemas.User).filter(schemas.User.id == user_id).delete()
        self.db.commit()
