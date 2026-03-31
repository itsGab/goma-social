from pydantic import EmailStr
from sqlmodel import SQLModel

from .validators import ValidPassword, ValidUsername


class UserInput(SQLModel):
    email: EmailStr
    username: ValidUsername
    password: ValidPassword


class UserPublic(SQLModel):
    email: str
    username: str
    id: int


class UserList(SQLModel):
    userlist: list[UserPublic]
