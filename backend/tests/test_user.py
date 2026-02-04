from sqlmodel import select

from app.models import User


def test_create_user(session):
    new_user = User(username='gabriel', password='12345')
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    statement = select(User).where(User.username == 'gabriel')
    user = session.exec(statement).first()

    assert user is not None
    assert user.username == 'gabriel'
    assert user.id is not None
    assert user.created_at is not None


def test_create_user_client(client):
    user_input = {
        'username': 'gabriel',
        'password': '12345',
    }
    response = client.post(
        url='/users/create',
        json=user_input,
    )
    # ! add assert status_code
    data = response.json()

    assert data['username'] == 'gabriel'
    assert data['id'] == 1


def test_list_user_client(client, user):
    response = client.get(
        url='/users/list',
    )
    # ! add assert status_code
    data = response.json()

    assert data == {
        'publiclist': [
            {
                'id': user.id,
                'username': user.username,
            }
        ]
    }
