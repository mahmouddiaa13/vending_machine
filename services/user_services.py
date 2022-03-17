from handlers.password_handler import hash_password
from infrastructure.repository.users.users_base_repo import UsersBaseRepo
from models.user import UserCreate, UserUpdate
from utils.exceptions import not_found, unprocessable_entity, unauthorized
from sqlalchemy.exc import IntegrityError


class UsersServices:
    def __init__(self, repo: UsersBaseRepo):
        self.repo = repo

    async def create_user(self, user: UserCreate):
        user.password = hash_password(user.password)
        user = await self.repo.create_user(user)
        return user

    async def get_user(self, user_id, current_user):
        user = await self.repo.get_user(user_id)
        if not user:
            raise not_found("user")

        if user_id != current_user.id:
            raise unauthorized

        return user

    async def update_user(self, user_id: int, updated_user: UserUpdate, current_user):
        user = await self.get_user(user_id, current_user)
        if updated_user.username:
            user.username = updated_user.username
        if updated_user.password:
            user.password = hash_password(updated_user.password)
        try:
            await self.repo.update_user(user_id, user)
        except IntegrityError:
            raise unprocessable_entity("username already taken!")
        return user

    async def delete_user(self, user_id: int, current_user):
        _ = await self.get_user(user_id, current_user)
        await self.repo.delete_user(user_id)
