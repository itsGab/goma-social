from datetime import datetime

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

from .schemas import FriendStatus

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


class User(TimestampModel, table=True):
    email: str = Field(unique=True, index=True)
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


class Profile(BaseSQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    display_name: str = Field(nullable=False)
    bio: str = Field(default='Sou novo aqui!')

    user_id: int = Field(
        default=None, foreign_key='user.id', ondelete='CASCADE', nullable=False
    )
    user: User = Relationship(back_populates='profile')


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
