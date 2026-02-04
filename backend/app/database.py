from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

from .settings import settings

engine = create_engine(settings.DATABASE_URL)


def get_session():
    with Session(
        engine, expire_on_commit=False
    ) as session:  # pragma: no cover
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
