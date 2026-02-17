# =============================================================================
#                  cenários de autenticação (token)
# =============================================================================

from http import HTTPStatus

from app.exceptions import ResponseMessage


# endpoint: /auth/token =======================================================
# !. post token success
def test_auth_token_success(client, user):
    login_data = {'username': user.email, 'password': user.clean_password}
    response = client.post('/auth/token', data=login_data)
    assert response.status_code == HTTPStatus.OK
    token_data = response.json()
    assert 'access_token' in token_data
    assert token_data['token_type'] == 'bearer'


# !. post token not registered user fail
def test_auth_token_user_not_found_fail(client):
    login_data = {'username': 'not@registered.com', 'password': 'hello-world'}
    response = client.post('/auth/token', data=login_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    data = response.json()
    assert data == {'detail': ResponseMessage.AUTH_INVALID_CREDENTIALS}


# !. post token wrong password fail
def test_auth_token_wrong_password_fail(client, user):
    login_data = {'username': user.email, 'password': 'wrong-pass'}
    response = client.post('/auth/token', data=login_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST
    data = response.json()
    assert data == {'detail': ResponseMessage.AUTH_INVALID_CREDENTIALS}


# !. post token missing field fail
def test_auth_token_missing_field_fail(client, user):
    login_data = {'username': user.email}
    response = client.post('/auth/token', data=login_data)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    data = response.json()
    # erro do OAuth2PasswordRequestForm
    assert data['detail'][0]['msg'] == 'Field required'


# endpoint: /auth/refresh-token ===============================================
# !. post refresh token success
def test_auth_refresh_token_success(client, access_token):
    response = client.post(
        '/auth/refresh-token',
        headers={
            'Authorization': f'Bearer {access_token}',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert 'access_token' in response.json()
    assert 'token_type' in response.json()


# !. post refresh token no token fail
def test_auth_refresh_token_without_token_fail(client):
    response = client.post(
        '/auth/refresh-token',
        headers={},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    # erro do OAuth2PasswordRequestForm
    assert response.json() == {'detail': 'Not authenticated'}


# !. post refresh token invalid token fail
def test_auth_refresh_token_with_invalid_token_fail(client):
    # invalid access_token
    response = client.post(
        '/auth/refresh-token',
        headers={
            'Authorization': 'Bearer not-a-valid-token',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': ResponseMessage.AUTH_NOT_AUTHORIZED}


def test_auth_refresh_token_with_invalid_basic_token_fail(
    client, access_token
):
    # not bearer
    response = client.post(
        '/auth/refresh-token',
        headers={
            'Authorization': f'Basic {access_token}',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}


def test_auth_refresh_token_with_invalid_empty_token_fail(client):
    # authorization empty
    response = client.post(
        '/auth/refresh-token',
        headers={
            'Authorization': '',
        },
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}


def test_auth_refresh_token_with_empty_auth_headers_fail(client):
    # authorization empty
    response = client.post(
        '/auth/refresh-token',
        headers={},
    )
    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}


# !. post refresh token expired token fail
# TODO: implementar teste de token expirado!!!
