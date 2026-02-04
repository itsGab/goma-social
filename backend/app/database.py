from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine

db_file_name = 'database.db'
db_url = f'sqlite:///{db_file_name}'

engine = create_engine(db_url)


def get_session():
    with Session(engine, expire_on_commit=False) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
