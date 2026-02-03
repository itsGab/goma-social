from sqlmodel import Field, SQLModel


class UserInput(SQLModel):
    username: str
    password: str


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str


class UserPublic(SQLModel):
    id: int
    username: str


class UserPublicList(SQLModel):
    publiclist: list[UserPublic]
