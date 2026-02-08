from datetime import datetime, timedelta
from typing import Annotated
from zoneinfo import ZoneInfo

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt import DecodeError, decode, encode
from pwdlib import PasswordHash
from sqlalchemy import select

from .database import SessionDep
from .exceptions import UnauthorizedException
from .models import User
from .settings import settings

pwd_context = PasswordHash.recommended()

oath2_scheme = OAuth2PasswordBearer(
    tokenUrl='/auth/token', refreshUrl='/auth/token-refresh'
)

DepTokenResponse = Annotated[str, Depends(oath2_scheme)]
DepTokenRequest = Annotated[OAuth2PasswordRequestForm, Depends()]


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo('UTC')) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTOS
    )
    to_encode.update({'exp': expire})
    encoded_jwt = encode(
        payload=to_encode,
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
    return encoded_jwt


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(password=plain_password, hash=hashed_password)


async def get_current_user(session: SessionDep, token: DepTokenResponse):
    try:
        payload = decode(
            jwt=token, key=settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        subject_email = payload.get('sub')
        if not subject_email:
            raise UnauthorizedException()
    except DecodeError:
        raise UnauthorizedException()
    user = await session.scalar(
        select(User).where(User.email == subject_email)
    )
    if not user:
        raise UnauthorizedException()
    return user


DepCurrentUser = Annotated[User, Depends(get_current_user)]
