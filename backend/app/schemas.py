from sqlmodel import SQLModel


class UserInput(SQLModel):
    username: str
    password: str


class User(SQLModel):
    id: int | None = None
    username: str
    password: str


class UserPublic(SQLModel):
    id: int
    username: str


class UserPublicList(SQLModel):
    publiclist: list[UserPublic]
