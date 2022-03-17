from fastapi import APIRouter, Depends

from infrastructure.db_conn.pg_sql_alchemy import get_sql_db
from infrastructure.repository.users.users_base_repo import VMBaseRepo
from services.products_services import PostsServices

router = APIRouter(prefix="/products")


@router.get("/")
def get_all_posts(repository: VMBaseRepo = Depends(get_sql_db)):
    posts_services = PostsServices(repository)
    posts = posts_services.get_all_posts()
    return posts


# @router.get("/{product_id}")
# def get_post(
#         post_id: int,
#         repository: SocialBaseRepo = Depends(get_sql_db)):
#     posts_services = PostsServices(repository)
#     posts = posts_services.get_post(post_id)
#     return posts
#
#
# @router.post(
#     "/",
#     status_code=status.HTTP_201_CREATED
# )
# def create_post(
#         post: Post,
#         repository: SocialBaseRepo = Depends(get_sql_db)
# ):
#     posts_services = PostsServices(repository)
#     post = posts_services.create_post(post)
#     return post
#
#
# @router.delete(
#     "/{post_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# def delete_post(
#         post_id: int,
#         repository: SocialBaseRepo = Depends(get_sql_db)
# ):
#     posts_services = PostsServices(repository)
#     posts_services.delete_post(post_id)
