from fastapi import APIRouter, Depends, status, Response

from infrastructure.repository.users.users_postgres_repo import UsersPostgresRepo
from infrastructure.repository.users.users_base_repo import UsersBaseRepo
from models.user import UserCreate, UserUpdate, UserResponse
from services.user_services import UsersServices
from utils.oauth2 import get_current_user

router = APIRouter(prefix="/users")


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse
)
async def create_user(
        user: UserCreate,
        repository: UsersBaseRepo = Depends(UsersPostgresRepo)
):
    users_services = UsersServices(repository)
    user = await users_services.create_user(user)
    return user


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse
)
async def get_user(
        user_id: int,
        current_user=Depends(get_current_user),
        repository: UsersBaseRepo = Depends(UsersPostgresRepo)
):
    users_services = UsersServices(repository)
    user = await users_services.get_user(user_id, current_user)
    return user


@router.patch(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse
)
async def update_user(
        user_id: int,
        updated_user: UserUpdate,
        current_user=Depends(get_current_user),
        repository: UsersBaseRepo = Depends(UsersPostgresRepo)
):
    users_services = UsersServices(repository)
    user = await users_services.update_user(user_id, updated_user, current_user)
    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_user(
        user_id: int,
        current_user=Depends(get_current_user),
        repository: UsersBaseRepo = Depends(UsersPostgresRepo)):
    users_services = UsersServices(repository)
    await users_services.delete_user(user_id, current_user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
