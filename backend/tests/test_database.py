import pytest
from sqlalchemy import select

from app.models import User


@pytest.mark.asyncio
async def test_create_user(session):
    new_user = User(
        email='test@test.com',
        username='test',
        password='test123',
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    statement = select(User).where(User.username == 'test')
    result = await session.execute(statement)
    user = result.scalar_one_or_none()

    assert user is not None
    assert user.username == 'test'
    assert user.id is not None
    assert user.created_at is not None
