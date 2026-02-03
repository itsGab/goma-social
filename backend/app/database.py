from sqlmodel import Session, SQLModel, create_engine

from .models import User

db_file_name = 'database.db'
db_url = f'sqlite:///{db_file_name}'

engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine, expire_on_commit=False) as session:
        yield session
