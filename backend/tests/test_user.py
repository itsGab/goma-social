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


def test_create_user_client(client):
    user_input = {
        'email': 'test@test.com',
        'username': 'test',
        'password': 'test123',
    }
    response = client.post(
        url='/users/create',
        json=user_input,
    )
    # ! add assert status_code
    data = response.json()

    assert data['username'] == 'test'
    assert data['id'] == 1


def test_not_auth_user_try_listclient(client, user):
    response = client.get(
        url='/users/list',
    )
    # ! add assert status_code
    data = response.json()

    assert data == {'detail': 'Not authenticated'}
