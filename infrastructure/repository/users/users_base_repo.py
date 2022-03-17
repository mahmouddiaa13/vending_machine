from models.user import UserCreate, UserUpdate


class UsersBaseRepo:
    async def create_user(self, user: UserCreate):
        raise NotImplementedError()

    async def get_user(self, user_id: int):
        raise NotImplementedError()

    async def update_user(self, user_id: int, updated_user: UserCreate):
        raise NotImplementedError()

    async def delete_user(self, user_id: int):
        raise NotImplementedError()
