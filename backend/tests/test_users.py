# =============================================================================
#                         cenários de usuários
# =============================================================================

from http import HTTPStatus
from unittest.mock import patch

from sqlalchemy.exc import IntegrityError

from app.exceptions import ResponseMessage
from app.models import UserPublic


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


# !. delete user fail username doesn't match
def test_user_delete_fail_username_doesnt_match(
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


# integrity error
def test_user_delete_fail_integrity_error(client, session, user, access_token):
    with patch.object(
        session,
        'commit',
        side_effect=IntegrityError(None, None, Exception()),
    ):
        response = client.request(
            method='DELETE',
            url='/users/delete',
            headers={'Authorization': f'Bearer {access_token}'},
            json={'username': user.username, 'password': user.clean_password},
        )
        data = response.json()

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert data == {'detail': 'Integrity Error'}
