from typing import Annotated

from fastapi import Query
from sqlmodel import Field, SQLModel

from ..constants import PAGE_DEFAULT_SIZE, PAGE_MAX_PAGES, PAGE_MAX_SIZE


class MessageResponse(SQLModel):
    message: str


class ErrorResponse(SQLModel):
    detail: str


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
