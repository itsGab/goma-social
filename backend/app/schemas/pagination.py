from typing import Annotated

from fastapi import Query
from sqlmodel import Field, SQLModel

PAGE_DEFAULT_SIZE = 20
PAGE_MAX_SIZE = 100
PAGE_MAX_PAGES = 100


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
