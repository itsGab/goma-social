# =============================================================================
#                         teste exceptions.py
# =============================================================================

from http import HTTPStatus

from fastapi import HTTPException

from app.exceptions import (
    AppException,
    NotFoundException,
    ResponseMessage,
    UserConflictException,
)


# default: http exception =====================================================
# !. standard behavior of http exception
def test_exception_http_exception():
    data = HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    assert data.status_code == HTTPStatus.BAD_REQUEST
    assert data.detail == 'Bad Request'


# customs:app exception ======================================================
# !. standard behavior of app exception
def test_exception_app_exception_base():
    data = AppException()
    assert data.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert data.detail == 'Internal Server Error'


def test_exception_app_exception_base_status():
    data = AppException(status_code=HTTPStatus.BAD_REQUEST)
    assert data.status_code == HTTPStatus.BAD_REQUEST
    assert data.detail == 'Bad Request'


def test_exception_app_exception_base_detail():
    er_msg = 'Integrity Error!!!'
    data = AppException(
        HTTPStatus.BAD_REQUEST, detail=f'Integrity Error: {er_msg}'
    )
    assert data.status_code == HTTPStatus.BAD_REQUEST
    assert '!!!' in data.detail


# !. kinds of user conlfict exception
def test_exception_kind_in_user_conflict_exception():
    # empty: kind default = 'any'
    data = UserConflictException()
    assert data.status_code == HTTPStatus.CONFLICT
    assert data.detail == ResponseMessage.USER_ANY_CONFLICT

    # username: kind = 'username'
    data = UserConflictException(kind='username')
    assert data.status_code == HTTPStatus.CONFLICT
    assert data.detail == ResponseMessage.USER_USERNAME_CONFLICT

    # email: kind (positional arg) = 'email'
    data = UserConflictException('email')
    assert data.status_code == HTTPStatus.CONFLICT
    assert data.detail == ResponseMessage.USER_EMAIL_CONFLICT

    # any : kind (positional arg) = 'any'
    data = UserConflictException('any')
    assert data.status_code == HTTPStatus.CONFLICT
    assert data.detail == ResponseMessage.USER_ANY_CONFLICT

    # detail: kind default + detail (postional arg) = 'message...'
    message = 'Testing detail message'
    data = UserConflictException(detail=message)
    assert data.status_code == HTTPStatus.CONFLICT
    assert data.detail == message

    # invalid kind: kind = 'invalid_key' (not registered as an option)
    data = UserConflictException(kind='invalid_key')
    assert data.detail == ResponseMessage.USER_ANY_CONFLICT


# !. whats of not found exception
def test_exception_what_in_not_found_exception():
    # empty: what default = 'default'
    data = NotFoundException()
    assert data.status_code == HTTPStatus.NOT_FOUND
    assert data.detail == ResponseMessage.NOT_FOUND_DEFAULT

    # user: what = 'user'
    data = NotFoundException('user')
    assert data.status_code == HTTPStatus.NOT_FOUND
    assert data.detail == ResponseMessage.NOT_FOUND_USER

    # profile: what (explicit) = 'profile'
    data = NotFoundException(what='profile')
    assert data.status_code == HTTPStatus.NOT_FOUND
    assert data.detail == ResponseMessage.NOT_FOUND_PROFILE

    # detail
    message = 'Testing detail message'
    data = NotFoundException(detail=message)
    assert data.status_code == HTTPStatus.NOT_FOUND
    assert data.detail == message

    # invalid
    data = NotFoundException(what='invalid')
    assert data.detail == ResponseMessage.NOT_FOUND_DEFAULT


# !. outros
def test_exception_inheritance():
    assert isinstance(AppException(), HTTPException)
    assert isinstance(UserConflictException(), AppException)


def test_exception_with_headers():
    headers = {'X-Error': 'CustomError'}
    data = UserConflictException(headers=headers)
    assert data.headers == headers
