from infrastructure.repository.users.users_base_repo import SocialBaseRepo
from models.product import Post


class PostsServices:
    def __init__(self, repo: SocialBaseRepo) -> None:
        self.repo = repo

    def get_all_posts(self):
        posts = self.repo.get_all_posts()
        return posts

    def get_post(self, post_id: int):
        post = self.repo.get_post(post_id)
        return post

    def create_post(self, post: Post) -> Post:
        post = self.repo.create_post(post)
        return post

    def delete_post(self, post_id: int):
        self.repo.delete_post(post_id)
