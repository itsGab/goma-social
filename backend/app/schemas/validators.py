from typing import Annotated

from pydantic import AfterValidator, BeforeValidator, Field, SecretStr

NAME_MIN_LEN = 3
NAME_MAX_LEN = 20

USERNAME_PATTERN = r'^[a-z0-9_]+$'
DISPLAY_NAME_PATTERN = r'^[a-zA-Z0-9_ ]+$'

PASSWORD_MIN_LEN = 8
PASSWORD_MAX_LEN = 20

BIO_MAX_LEN = 1000


def trim_string(name: str) -> str:
    return name.strip()


def trim_string_lower(name: str) -> str:
    return trim_string(name).lower()


def validate_password_complexity(value: SecretStr) -> SecretStr:
    password = value.get_secret_value()

    if not any(char.isdigit() for char in password):
        raise ValueError('A senha deve conter pelo menos um número')
    if not any(char.isupper() for char in password):
        raise ValueError('A senha deve conter pelo menos uma letra maiúscula')
    if not any(char.islower() for char in password):
        raise ValueError('A senha deve conter pelo menos uma letra minúscula')
    if not any(not char.isalnum() for char in password):
        raise ValueError(
            'A senha deve conter pelo menos um símbolo (ex: @, #, $, %)'
        )

    return value


ValidPassword = Annotated[
    SecretStr,
    Field(
        min_length=PASSWORD_MIN_LEN,
        max_length=PASSWORD_MAX_LEN,
        description='Senha forte com maiúscula, minúscula, números e símbolos',
    ),
    AfterValidator(validate_password_complexity),
]


ValidUsername = Annotated[
    str,
    BeforeValidator(trim_string_lower),
    Field(
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN,
        pattern=USERNAME_PATTERN,
        description='Apenas letras minúsculas, números e underscores',
    ),
]


# TODO: fazer teste com espaco no nome
ValidName = Annotated[
    str,
    BeforeValidator(trim_string),
    Field(
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN,
        pattern=DISPLAY_NAME_PATTERN,
        description='Apenas letras, números, underscores e espaços entre '
        + 'palavras',
    ),
]
