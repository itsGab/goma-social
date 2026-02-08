from enum import Enum
from http import HTTPStatus

from fastapi import HTTPException


class ResponseMessage(str, Enum):
    # user
    USER_ANY_CONFLICT = 'Usuário ou email já cadastrado'
    USER_USERNAME_CONFLICT = 'Nome de usuário já cadastrado'
    USER_EMAIL_CONFLICT = 'Email já cadastrado'
    USER_DELETED_SUCCESS = 'Conta deletada com sucesso'

    # auth
    AUTH_INVALID_CREDENTIALS = 'Email ou senha incorretos'
    AUTH_NOT_AUTHORIZED = 'Não autorizado'

    # data validation
    DATA_MISSING_FIELDS = 'Pelo menos um campo deve ser fornecido'


class AppException(HTTPException):
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR  # Padrão
    detail = 'Erro interno no servidor'
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

    def __init__(self, kind: str = 'any', detail: str | None = None):
        message = detail or self.MAP.get(
            kind.lower(), ResponseMessage.USER_ANY_CONFLICT
        )
        super().__init__(detail=message)
