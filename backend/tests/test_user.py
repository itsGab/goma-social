from http import HTTPStatus

from app.exceptions import ResponseMessage
from app.models import UserPublic


def test_user_create_new_user_success(client):
    user_input = {
        'email': 'test@test.com',
        'username': 'test',
        'password': 'test123',
    }
    response = client.post(
        url='/users/create',
        json=user_input,
    )

    assert response.status_code == HTTPStatus.CREATED

    data = response.json()
    assert data['username'] == 'test'
    assert data['id'] == 1


def test_list_users_user_not_authenticated_error(client):
    response = client.get(
        url='/users/list', headers={'Authorization': 'Bearer invalid-token'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED

    data = response.json()
    # aqui o erro é pego pelo oath2_scheme.
    assert data == {'detail': ResponseMessage.AUTH_NOT_AUTHORIZED}


def test_list_users_user_authenticated_success(client, user, token):
    response = client.get(
        url='/users/list',
        headers={'Authorization': f'Bearer {token["access_token"]}'},
    )

    assert response.status_code == HTTPStatus.OK

    data = response.json()
    user_data = user.model_dump()
    user_public = UserPublic(**user_data).model_dump()
    assert data == {'userlist': [user_public]}


def test_user_create_user_username_conflict_error(client, user):
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


def test_user_create_user_email_conflict_error(client, user):
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
