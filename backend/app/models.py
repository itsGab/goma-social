from datetime import datetime
from enum import Enum

from pydantic import EmailStr
from sqlalchemy import MetaData
from sqlmodel import (
    CheckConstraint,
    Column,
    DateTime,
    Field,
    Relationship,
    SQLModel,
    func,
)

# Define um padrão de nomes para as restrições
convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = MetaData(naming_convention=convention)


class BaseSQLModel(SQLModel):
    metadata = metadata


class TimestampModel(BaseSQLModel):
    # campos para horario da criacao e atualizacao
    # ! TODO: revisar
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


class UserInput(SQLModel):
    email: EmailStr
    username: str
    password: str


class User(TimestampModel, table=True):
    email: EmailStr = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    id: int | None = Field(default=None, primary_key=True)
    password: str = Field(nullable=False)

    profile: 'Profile' = Relationship(
        back_populates='user',
        sa_relationship_kwargs={'cascade': 'all, delete-orphan'},
    )

    posts: list['Post'] = Relationship(
        back_populates='author',
        sa_relationship_kwargs={'cascade': 'all, delete-orphan'},
    )


class UserPublic(SQLModel):
    email: EmailStr
    username: str
    id: int


class UserOnDelete(SQLModel):
    username: str
    password: str


class UserList(SQLModel):
    userlist: list[UserPublic]


class Token(SQLModel):
    access_token: str
    token_type: str


class ErrorMessage(SQLModel):
    detail: str


class Profile(BaseSQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    display_name: str = Field(nullable=False)
    bio: str = Field(default='Sou novo aqui!')

    user_id: int = Field(
        default=None, foreign_key='user.id', ondelete='CASCADE', nullable=False
    )
    user: User = Relationship(back_populates='profile')


class ProfilePublic(SQLModel):
    display_name: str
    bio: str


class ProfileOnUpdate(SQLModel):
    display_name: str | None = Field(default=None)
    bio: str | None = Field(default=None)


class RegularMessage(SQLModel):
    message: str


class Post(BaseSQLModel, table=True):
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), index=True
        ),
    )
    id: int = Field(default=None, primary_key=True)
    content: str

    user_id: int = Field(
        foreign_key='user.id', ondelete='CASCADE', nullable=False
    )
    author: User = Relationship(back_populates='posts')


class PostInput(SQLModel):
    content: str


class PostPublic(SQLModel):
    id: int = Field(serialization_alias='post_id')
    content: str
    author: UserPublic
    created_at: datetime


class ListPosts(SQLModel):
    posts: list[PostPublic]


class FriendStatus(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    BLOCKED = 'blocked'


class Friendship(BaseSQLModel, table=True):
    __table_args__ = (
        CheckConstraint('user_id1 < user_id2', name='check_ordered_ids'),
    )
    user_id1: int = Field(foreign_key='user.id', primary_key=True)
    user_id2: int = Field(foreign_key='user.id', primary_key=True)
    # deveria settar requested_id como index ou pk?
    requested_by: int = Field(foreign_key='user.id', index=True)
    status: FriendStatus = Field(default=FriendStatus.PENDING)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
