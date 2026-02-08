from fastapi import APIRouter
from sqlalchemy import select

from ..database import SessionDep
from ..exceptions import InvalidUnauthorizedException
from ..models import Token, User
from ..security import (
    DepCurrentUser,
    DepTokenRequest,
    create_access_token,
    verify_password,
)

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: DepTokenRequest, session: SessionDep
):
    user = await session.scalar(
        select(User).where(User.email == form_data.username)
    )
    if not user:
        raise InvalidUnauthorizedException()
    if not verify_password(form_data.password, user.password):
        raise InvalidUnauthorizedException()
    access_token = create_access_token(data={'sub': user.email})
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh-token', response_model=Token)
def refresh_access_token(current_user: DepCurrentUser):
    new_access_token = create_access_token(data={'sub': current_user.email})
    return {'access_token': new_access_token, 'token_type': 'bearer'}
