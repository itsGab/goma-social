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

    # data validation
    DATA_MISSING_FIELDS = 'At least one field must be provided'

    # padrao
    INTERNAL_SERVER_ERROR = 'Internal server error'


class AppException(HTTPException):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR
    detail = ResponseMessage.INTERNAL_SERVER_ERROR
    headers = None

    def __init__(
        self, detail: str = None, status_code: int = None, headers: dict = None
    ):
        super().__init__(
            status_code=status_code or self.status_code,
            detail=detail or self.detail,
            headers=headers or self.headers,
        )


class UnauthorizedException(AppException):
    status_code = HTTPStatus.UNAUTHORIZED
    detail = ResponseMessage.AUTH_NOT_AUTHORIZED
    headers = {'WWW-Authenticate': 'Bearer'}


class InvalidUnauthorizedException(AppException):
    status_code = HTTPStatus.BAD_REQUEST
    detail = ResponseMessage.AUTH_INVALID_CREDENTIALS


class UserConflictException(AppException):
    """
    Exceção pode ser usada para conflitos genéricos, de username ou de e-mail,
    utilizando as mensagens padronizadas do ResponseMessage.

    Args:
        kind (str):
            O tipo de conflito ('any', 'username', 'email'). Defaults to 'any'.
        detail (str, optional):
            Mensagem customizada que sobrescreve o padrão do MAP.
    """

    status_code = HTTPStatus.CONFLICT
    MAP = {
        'any': ResponseMessage.USER_ANY_CONFLICT,
        'username': ResponseMessage.USER_USERNAME_CONFLICT,
        'email': ResponseMessage.USER_EMAIL_CONFLICT,
    }

    def __init__(self, kind: str = 'any', detail: str | None = None, **kwargs):
        message = detail or self.MAP.get(
            kind.lower(), ResponseMessage.USER_ANY_CONFLICT
        )
        super().__init__(detail=message, **kwargs)
