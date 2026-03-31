from sqlmodel import Field, SQLModel

from ..constants import BIO_MAX_LEN, NAME_MAX_LEN, NAME_MIN_LEN


class ProfilePublic(SQLModel):
    display_name: str
    bio: str


class ProfileOnUpdate(SQLModel):
    display_name: str | None = Field(
        default=None, min_length=NAME_MIN_LEN, max_length=NAME_MAX_LEN
    )
    bio: str | None = Field(default=None, max_length=BIO_MAX_LEN)
