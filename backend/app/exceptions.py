from enum import Enum
from http import HTTPStatus

from fastapi import HTTPException


class ResponseMessage(str, Enum):
    # user
    USER_ANY_CONFLICT = 'Username or email already in use'
    USER_USERNAME_CONFLICT = 'Username already in use'
    USER_EMAIL_CONFLICT = 'Email already in use'
    USER_DELETED_SUCCESS = 'User deleted successfully'

    # auth
    AUTH_INVALID_CREDENTIALS = 'Invalid email or password'
    AUTH_NOT_AUTHORIZED = 'Not authorized'

    # not found
    NOT_FOUND_DEFAULT = 'Not Found'
    NOT_FOUND_USER = 'User not found'
    NOT_FOUND_PROFILE = 'Profile not found'


UnauthorizedException = HTTPException(
    status_code=HTTPStatus.UNAUTHORIZED,
    detail=ResponseMessage.AUTH_NOT_AUTHORIZED,
    headers={'WWW-Authenticate': 'Bearer'},
)

InvalidUnauthorizedException = HTTPException(
    status_code=HTTPStatus.BAD_REQUEST,
    detail=ResponseMessage.AUTH_INVALID_CREDENTIALS,
)
