# =============================================================================
#                         cenários de banco de dados
# =============================================================================

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app.models import User


# database: table user ========================================================
# !. add user to database success
@pytest.mark.asyncio
async def test_database_add_user_success(session):
    new_user = User(
        username='test_db',
        email='test@db.com',
        password='test_db_123',
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    statement = select(User).where(User.username == new_user.username)
    result = await session.execute(statement)
    user = result.scalar_one_or_none()
    user_json = user.json()

    assert user.username == new_user.username
    assert user.email == new_user.email
    assert user.password == new_user.password
    assert user.id == 1
    assert 'created_at' in user_json
    assert 'updated_at' in user_json


# !. add user missing username fail
@pytest.mark.asyncio
async def test_database_add_user_missing_username_fail(session):
    new_user = User(
        # username='test_db',
        email='test@db.com',
        password='test_db_123',
    )
    session.add(new_user)
    with pytest.raises(IntegrityError):
        await session.commit()
    await session.rollback()
    statement = select(User).where(User.email == new_user.email)
    result = await session.execute(statement)
    user = result.scalar_one_or_none()

    assert user is None


# !. add user missing email fail
@pytest.mark.asyncio
async def test_database_add_user_missing_email_fail(session):
    new_user = User(
        username='test_db',
        # email='test@db.com',
        password='test_db_123',
    )
    session.add(new_user)
    with pytest.raises(IntegrityError):
        await session.commit()
    await session.rollback()
    statement = select(User).where(User.username == new_user.username)
    result = await session.execute(statement)
    user = result.scalar_one_or_none()

    assert user is None


# !. add user missing password fail
@pytest.mark.asyncio
async def test_database_add_user_missing_password_fail(session):
    new_user = User(
        username='test_db',
        email='test@db.com',
        # password='test_db_123',
    )
    session.add(new_user)
    with pytest.raises(IntegrityError):
        await session.commit()
    await session.rollback()
    statement = select(User).where(User.username == new_user.username)
    result = await session.execute(statement)
    user = result.scalar_one_or_none()

    assert user is None
