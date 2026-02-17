# =============================================================================
#                         cenários de usuários
# =============================================================================

from http import HTTPStatus

import pytest
from sqlmodel import select

from app.exceptions import ResponseMessage
from app.models import Profile, UserPublic


# endpoint: /users/create =====================================================
# !. post user create success
def test_user_create_new_user_success(client):
    new_user = {
        'email': 'test@test.com',
        'username': 'test',
        'password': 'test123',
    }
    response = client.post(
        url='/users/create',
        json=new_user,
    )

    assert response.status_code == HTTPStatus.CREATED

    data = response.json()
    assert data['username'] == new_user['username']
    assert data['id'] == 1


# !. post user create username is use username conflict
def test_user_create_user_username_conflict_fail(client, user):
    response = client.post(
        url='/users/create',
        json={
            'username': user.username,
            'email': 'whatever@mail.com',
            'password': 'pwd321',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT

    data = response.json()
    assert data == {'detail': ResponseMessage.USER_ANY_CONFLICT}


# !. post user create email in use email conflict
def test_user_create_user_email_conflict_fail(client, user):
    response = client.post(
        url='/users/create',
        json={
            'username': 'whatever',
            'email': user.email,
            'password': 'pwd321',
        },
    )

    assert response.status_code == HTTPStatus.CONFLICT

    data = response.json()
    assert data == {'detail': ResponseMessage.USER_ANY_CONFLICT}


# endpoint: /users/delete =====================================================
# !. post user delete success
def test_user_delete_user_success(client, user, session, access_token):
    response = client.request(
        method='DELETE',
        url='/users/delete',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'username': user.username, 'password': user.clean_password},
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json()['message'] == 'User deleted successfully'


# !. post user delete username dont match fail
def test_user_delete_username_dont_match_fail(
    client, user, session, access_token
):
    response = client.request(
        method='DELETE',
        url='/users/delete',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'username': 'wrong-user', 'password': user.clean_password},
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert (
        response.json()['detail']
        == "Username provided doesn't match the current user"
    )


# !. post user delete wrong password fail
def test_user_delete_wrong_password_fail(client, user, session, access_token):
    response = client.request(
        method='DELETE',
        url='/users/delete',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'username': user.username, 'password': 'wrong-password'},
    )
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.json()['detail'] == 'Wrong password'


# endpoint: /users/list =======================================================
# !. get user list success
def test_list_users_user_authenticated_success(client, user, access_token):
    response = client.get(
        url='/users/list',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    assert response.status_code == HTTPStatus.OK

    data = response.json()
    user_data = user.model_dump()
    user_public = UserPublic(**user_data).model_dump()
    assert data == {'userlist': [user_public]}


# !. get user list no current user fail
def test_list_users_user_not_authenticated_error_fail(client):
    response = client.get(
        url='/users/list', headers={'Authorization': 'Bearer invalid-token'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED

    data = response.json()
    # aqui o erro é pego pelo oath2_scheme.
    assert data == {'detail': ResponseMessage.AUTH_NOT_AUTHORIZED}


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
        '/users/own_profile',
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
        '/users/own_profile',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    assert response.status_code == HTTPStatus.OK
    profile = response.json()
    assert profile['display_name'] == 'user-test'
    assert profile['bio'] == 'Sou novo aqui!'

    # only display name
    response = client.patch(
        '/users/own_profile/update',
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
        '/users/own_profile/update',
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
        '/users/own_profile/update',
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
        '/users/own_profile/update',
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
