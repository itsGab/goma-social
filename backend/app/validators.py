from typing import Annotated

from pydantic import AfterValidator, BeforeValidator, Field, SecretStr

from .constants import (
    NAME_MAX_LEN,
    NAME_MIN_LEN,
    PASSWORD_MAX_LEN,
    PASSWORD_MIN_LEN,
    USERNAME_PATTERN,
)


def trim_string(name: str | any) -> str:
    if isinstance(name, str):
        return name.strip().lower()
    return name


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
    BeforeValidator(trim_string),
    Field(
        min_length=NAME_MIN_LEN,
        max_length=NAME_MAX_LEN,
        pattern=USERNAME_PATTERN,  # se mudar para sqlalchemy deve ser pattern
        description='Apenas letras, números e underscores',
    ),
]
