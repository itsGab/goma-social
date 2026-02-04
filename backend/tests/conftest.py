import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, StaticPool, create_engine

from app import models
from app.database import get_session
from app.main import app


@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    models.SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

    models.SQLModel.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(name='client')
def client_fixture(session: Session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(name='user')
def user_fixture(session: Session):
    user = models.User(
        username='user01',
        password='password123',
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
