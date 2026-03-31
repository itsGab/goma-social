from datetime import datetime
from enum import Enum
from typing import Annotated

from fastapi import Query
from pydantic import AfterValidator, BeforeValidator, EmailStr, SecretStr
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

# IDEA: mover constantes para outro local.
BIO_MAX_LEN = 1000
PAGE_DEFAULT_SIZE = 20
PAGE_MAX_SIZE = 100
PAGE_MAX_PAGES = 100
POST_MAX_LEN = 1000
NAME_MIN_LEN = 3
NAME_MAX_LEN = 20

USERNAME_PATTERN = r'^[a-z0-9_]+$'
PASSWORD_MIN_SIZE = 8


def trim_string(name: str | any) -> str:
    if isinstance(name, str):
        return name.strip().lower()
    return name


def validate_password_complexity(value: SecretStr) -> SecretStr:
    password = value.get_secret_value()

    if not any(char.isdigit() for char in password):
        raise ValueError('A senha deve conter pelo menos um número')
    if not any(char.isupper() for char in password):
        raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
    if not any(char.islower() for char in password):
        raise ValueError('A senha deve conter pelo menos uma letra minúscula')
    if not any(not char.isalnum() for char in password):
        raise ValueError(
            'A senha deve conter pelo menos um símbolo (ex: @, #, $, %)'
        )

    return value


ValidPassword = Annotated[
    SecretStr,
    Field(
        min_length=8,
        max_length=40,
        description='Senha forte com maiúscula, minúscula, números e símbolos',
    ),
    AfterValidator(validate_password_complexity),
]


ValidUsername = Annotated[
    str,
    BeforeValidator(trim_string),
    Field(
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN,
        regex=USERNAME_PATTERN,  # se mudar para sqlalchemy deve ser pattern
        description='Apenas letras, números e underscores',
    ),
]


class BaseSQLModel(SQLModel):
    metadata = metadata


class TimestampModel(BaseSQLModel):
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        ),
    )
    updated_at: datetime | None = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        ),
    )


class UserInput(SQLModel):
    email: EmailStr
    username: ValidUsername
    password: ValidPassword


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
    email: str
    username: str
    id: int


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
    display_name: str | None = Field(
        default=None, min_length=NAME_MIN_LEN, max_length=NAME_MAX_LEN
    )
    bio: str | None = Field(default=None, max_length=BIO_MAX_LEN)


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
    author: User = Relationship(
        back_populates='posts', sa_relationship_kwargs={'lazy': 'selectin'}
    )


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


class FriendStatus(str, Enum):
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    BLOCKED = 'blocked'


class Friendship(BaseSQLModel, table=True):
    __table_args__ = (
        CheckConstraint('user_id1 < user_id2', name='check_ordered_ids'),
    )
    user_id1: int = Field(
        foreign_key='user.id', ondelete='CASCADE', primary_key=True
    )
    user_id2: int = Field(
        foreign_key='user.id', ondelete='CASCADE', primary_key=True
    )
    requested_by: int = Field(
        foreign_key='user.id', ondelete='CASCADE', index=True
    )
    blocked_by: int = Field(
        default=None, foreign_key='user.id', ondelete='CASCADE', nullable=True
    )
    status: FriendStatus = Field(default=FriendStatus.PENDING)
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )


class RequestType(str, Enum):
    RECEIVED = 'received'
    REQUESTED = 'requested'


class FriendRequest(SQLModel):
    friend_user_id: int
    friend_username: str
    friend_email: EmailStr
    status: FriendStatus
    created_at: datetime
    request_type: RequestType


class ListFriendRequest(SQLModel):
    pending: list[FriendRequest]


class FriendAction(str, Enum):
    ACCEPT = 'accept'
    REJECT = 'reject'


class FriendResponseRequest(SQLModel):
    friend_id: int
    action: FriendAction


class PageParams(SQLModel):
    page: int = Field(
        default=1,
        ge=1,
        lt=PAGE_MAX_PAGES,
        description='numeração da página (começa em 1)',
    )

    size: int = Field(
        default=PAGE_DEFAULT_SIZE,
        ge=1,
        le=PAGE_MAX_SIZE,
        description='quantidade de itens por página',
    )

    @property
    def limit(self) -> int:
        return self.size

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size


QueryPage = Annotated[PageParams, Query()]
