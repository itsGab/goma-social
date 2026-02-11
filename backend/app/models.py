from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import MetaData
from sqlmodel import Column, DateTime, Field, SQLModel, func

# Define um padrão de nomes para as restrições
convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = MetaData(naming_convention=convention)


class BaseModel(SQLModel):
    metadata = metadata


class TimestampModel(BaseModel):
    # campos para horario da criacao e atualizacao
    # ! TODO: revisar
    created_at: datetime = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), server_default=func.now()),
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
        ),
    )


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)


class UserInput(UserBase):
    password: str


class User(TimestampModel, UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str = Field(nullable=False)


class UserPublic(UserBase):
    id: int


class UserList(SQLModel):
    userlist: list[UserPublic]


class Token(SQLModel):
    access_token: str
    token_type: str


class ErrorMessage(SQLModel):
    detail: str
