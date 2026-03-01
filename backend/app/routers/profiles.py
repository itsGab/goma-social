from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from ..database import SessionDep
from ..exceptions import ResponseMessage
from ..models import Profile, ProfileOnUpdate, ProfilePublic
from ..security import DepCurrentUser

router = APIRouter(prefix='/profiles', tags=['profiles'])


@router.get(
    '/',
    response_model=ProfilePublic,
    status_code=HTTPStatus.OK,
    summary='Retorna próprio perfil',
    description='Retorna o próprio perfil do usuário com informações públicas',
)
async def get_profile(session: SessionDep, current_user: DepCurrentUser):
    query = select(Profile).where(
        Profile.user_id == current_user.id  # type: ignore
    )
    profile = await session.scalar(query)
    return profile


@router.patch(
    '/update',
    response_model=ProfilePublic,
    status_code=HTTPStatus.OK,
    summary='Atualiza o próprio perfil',
    description='Atualiza o próprio perfil do usuário com informações '
    'públicas',
)
async def update_profile(
    profile_data: ProfileOnUpdate,
    session: SessionDep,
    current_user: DepCurrentUser,
):
    query = select(Profile).where(Profile.user_id == current_user.id)
    profile_db = await session.scalar(query)
    if not profile_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=ResponseMessage.NOT_FOUND_PROFILE,
        )
    try:
        update_data = profile_data.model_dump(exclude_unset=True)
        profile_db.sqlmodel_update(update_data)
        session.add(profile_db)
        await session.commit()
        await session.refresh(profile_db)
        return profile_db
    except IntegrityError:
        await session.rollback()
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail='Integrity Error')
    except Exception:
        await session.rollback()
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR)
