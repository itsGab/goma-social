from http import HTTPStatus
from unittest.mock import patch

import pytest
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.models import Profile


# endpoint: /users/profile... =================================================
# !. profile created with user creation success
def test_profile_is_created_with_user_creation_success(client):
    user = client.post(
        '/users/create',
        json={
            'username': 'user-test',
            'email': 'test@mail.com',
            'password': 'test',
        },
    )
    assert user.status_code == HTTPStatus.CREATED

    token = client.post(
        '/auth/token', data={'username': 'test@mail.com', 'password': 'test'}
    )
    assert token.status_code == HTTPStatus.OK
    access_token = token.json()['access_token']

    response = client.get(
        '/profiles',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    profile = response.json()
    assert profile['display_name'] == 'user-test'
    assert profile['bio'] == 'Sou novo aqui!'


# !. profile update success
def test_profile_update_success(client):
    user = client.post(
        '/users/create',
        json={
            'username': 'user-test',
            'email': 'test@mail.com',
            'password': 'test',
        },
    )
    assert user.status_code == HTTPStatus.CREATED

    token = client.post(
        '/auth/token', data={'username': 'test@mail.com', 'password': 'test'}
    )
    assert token.status_code == HTTPStatus.OK
    access_token = token.json()['access_token']

    response = client.get(
        '/profiles',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    profile = response.json()
    assert profile['display_name'] == 'user-test'
    assert profile['bio'] == 'Sou novo aqui!'

    # only display name
    response = client.patch(
        '/profiles/update',
        json={'display_name': 'super user'},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'display_name': 'super user',
        'bio': 'Sou novo aqui!',
    }
    # only bio
    response = client.patch(
        '/profiles/update',
        json={'bio': "I'm the super user"},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'display_name': 'super user',
        'bio': "I'm the super user",
    }
    # both
    response = client.patch(
        '/profiles/update',
        json={
            'display_name': 'THE SUPER USER',
            'bio': "I'm THE SUPER USER",
        },
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'display_name': 'THE SUPER USER',
        'bio': "I'm THE SUPER USER",
    }
    # none
    response = client.patch(
        '/profiles/update',
        json={},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'display_name': 'THE SUPER USER',
        'bio': "I'm THE SUPER USER",
    }


# !. test user delete also delete the profile
@pytest.mark.asyncio
async def test_delete_profile_is_delete_with_user_deletion_success(
    client, session
):
    response = client.post(
        '/users/create',
        json={
            'username': 'user-test',
            'email': 'test@mail.com',
            'password': 'test',
        },
    )
    assert response.status_code == HTTPStatus.CREATED

    query = select(Profile).where(Profile.user_id == 1)
    profile_db = await session.scalar(query)
    assert profile_db
    assert profile_db.display_name == 'user-test'

    token = client.post(
        '/auth/token', data={'username': 'test@mail.com', 'password': 'test'}
    )
    assert token.status_code == HTTPStatus.OK
    access_token = token.json()['access_token']

    response = client.request(
        method='DELETE',
        url='/users/delete',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'username': 'user-test', 'password': 'test'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json()['message'] == 'User deleted successfully'

    query = select(Profile).where(Profile.user_id == 1)
    profile_db = await session.scalar(query)

    assert not profile_db


# test user without profile
def test_update_profile_fail_user_without_profile(client, user, access_token):
    response = client.patch(
        '/profiles/update',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'display_name': 'Harry Potter'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'Profile not found'}


def test_int(client, session):
    client.post(
        '/users/create',
        json={
            'username': 'user-test',
            'email': 'test@mail.com',
            'password': 'test',
        },
    )
    token = client.post(
        '/auth/token', data={'username': 'test@mail.com', 'password': 'test'}
    )
    assert token.status_code == HTTPStatus.OK
    access_token = token.json()['access_token']
    with patch.object(
        session,
        'commit',
        side_effect=IntegrityError(None, None, Exception()),
    ):
        response = client.patch(
            '/profiles/update',
            json={'display_name': 'super user'},
            headers={'Authorization': f'Bearer {access_token}'},
        )
        data = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert data == {'detail': 'Integrity Error'}
