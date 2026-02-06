import pytest_asyncio
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import StaticPool

from app import models
from app.database import get_session
from app.main import app


@pytest_asyncio.fixture(name='session')
async def session_fixture():
    engine = create_async_engine(
        'sqlite+aiosqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    async with engine.begin() as conn:
        await conn.run_sync(models.SQLModel.metadata.create_all)
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
    async with engine.begin() as conn:
        await conn.run_sync(models.SQLModel.metadata.drop_all)


@pytest_asyncio.fixture(name='client')
async def client_fixture(session: AsyncSession):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest_asyncio.fixture(name='user')
async def user_fixture(session: AsyncSession):
    user = models.User(
        username='user01',
        password='password123',
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
