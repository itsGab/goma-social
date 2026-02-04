from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, func


class TimestampModel(SQLModel):
    # campos para horario da criacao e atualizacao
    created_at: datetime = Field(
        default=None, sa_column=Column(DateTime, server_default=func.now())
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=Column(
            DateTime, server_default=func.now(), onupdate=func.now()
        ),
    )


class UserInput(SQLModel):
    username: str
    password: str


class User(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str


class UserPublic(SQLModel):
    id: int
    username: str


class UserPublicList(SQLModel):
    publiclist: list[UserPublic]
