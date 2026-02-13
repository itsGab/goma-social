# =============================================================================
#                               security.py
# =============================================================================

import pytest

from app.exceptions import UnauthorizedException
from app.security import create_access_token, get_current_user


# create_acess_token ==========================================================
# !. create acess token success
def something(): ...  # TODO: terminar os testes!!!


# get_password_hash ===========================================================


# verify_password =============================================================


# get_current_user ============================================================
# !. get current user success
@pytest.mark.asyncio
async def test_security_get_current_user_success(session, user):
    access_token = create_access_token(data={'sub': user.email})
    current_user = await get_current_user(session, access_token)

    assert current_user is not None
    assert current_user.username == user.username


# !. get current user missing subject fail
@pytest.mark.asyncio
async def test_security_get_current_user_missing_sub_fail(session, user):
    access_token = create_access_token(data={'missing': '???'})

    with pytest.raises(UnauthorizedException):
        await get_current_user(session, access_token)


# !. get current user decode error (invalid token) fail
@pytest.mark.asyncio
async def test_security_get_current_user_invalid_token(session, user):
    access_token = 'invalid-token'

    with pytest.raises(UnauthorizedException):
        await get_current_user(session, access_token)


# !. get current user not user fail
@pytest.mark.asyncio
async def test_security_get_current_user_user_not_found(session, user):
    access_token = create_access_token(data={'sub': 'nao@existe.com'})

    with pytest.raises(UnauthorizedException):
        await get_current_user(session, access_token)
