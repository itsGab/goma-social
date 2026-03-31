from datetime import datetime

from sqlmodel import Field, SQLModel

from ..constants import POST_MAX_LEN
from .user import UserPublic


class PostInput(SQLModel):
    content: str = Field(default=None, max_length=POST_MAX_LEN)


class PostPublic(SQLModel):
    id: int = Field(serialization_alias='post_id')
    content: str
    author: UserPublic
    created_at: datetime


class ListPosts(SQLModel):
    posts: list[PostPublic]
    limit: int
    offset: int
