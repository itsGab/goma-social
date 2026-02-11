from http import HTTPStatus

from fastapi import HTTPException

from app.exceptions import AppException, ResponseMessage, UserConflictException


def test_exception_http_exception():
    data = HTTPException(status_code=HTTPStatus.BAD_REQUEST)
    assert data.status_code == HTTPStatus.BAD_REQUEST
    assert data.detail == 'Bad Request'


def test_exception_app_exception_base():
    data = AppException()
    assert data.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert data.detail == ResponseMessage.INTERNAL_SERVER_ERROR


def test_exception_user_conflict_exception():
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
    assert data.detail == 'Testing detail message'
