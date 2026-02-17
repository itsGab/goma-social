from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from ..database import SessionDep
from ..exceptions import (
    HTTPException,
    UnauthorizedException,
    UserConflictException,
)
from ..models import (
    ErrorMessage,
    Profile,
    ProfileOnUpdate,
    ProfilePublic,
    RegularMessage,
    User,
    UserInput,
    UserList,
    UserOnDelete,
    UserPublic,
)
from ..security import DepCurrentUser, get_password_hash, verify_password

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/create',
    response_model=UserPublic,
    status_code=HTTPStatus.CREATED,
    summary='Cria usuário',
    description='Cria um usuário com username, email e password e salva no '
    'banco de dados.',
    responses={
        UserConflictException.status_code.value: {'model': ErrorMessage}
    },
)
async def create_user(
    user_input: UserInput, session: SessionDep
) -> UserPublic:
    """
    Realiza o cadastro do usuário com hash de senha e validação de duplicidade.
    Cria perfil (profile) para usuário.

    Raises:
        UserConflictException: Se username ou email já constarem na base.
    """
    # verifica conflito com o banco de dados
    query = select(User).where(
        (User.username == user_input.username)
        | (User.email == user_input.email)
    )
    db_user = await session.scalar(query)
    if db_user:
        raise UserConflictException()

    # sem conflito, cadastra new user
    hashed_password = get_password_hash(user_input.password)
    new_user = User(
        email=user_input.email,
        username=user_input.username,
        password=hashed_password,
    )

    # com new_user, cria new_profile
    new_profile = Profile(display_name=user_input.username, user=new_user)

    session.add(new_user)
    session.add(new_profile)
    await session.commit()
    await session.refresh(new_user)
    return new_user


@router.delete(
    '/delete',
    response_model=RegularMessage,
    status_code=HTTPStatus.OK,
    summary='Delete usuário',
    description='Delete usuário no banco de dados.',
)
async def delete_user(
    userdata: UserOnDelete, session: SessionDep, current_user: DepCurrentUser
):
    # confirma o nome do usuario para delecao
    if current_user.username != userdata.username:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST,
            detail="Username provided doesn't match the current user",
        )
    if not verify_password(userdata.password, current_user.password):
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail='Wrong password')
    try:
        await session.delete(current_user)
        await session.commit()
        return {'message': 'User deleted successfully'}
    except Exception as e:
        await session.rollback()
        er_msg = str(e.orig).lower()
        raise HTTPException(
            HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f'Internal Server Error: {er_msg}',
        )


@router.get(
    '/list',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    summary='Lista usuários',
    description='Faz a listagem de usuários com informações públicas.',
    responses={
        UnauthorizedException.status_code.value: {'model': ErrorMessage}
    },
)
async def list_users(session: SessionDep, current_user: DepCurrentUser):
    """
    Lista os usuários (Requer autenticação)

    Raises:
        UnauthorizedException: Se não estiver autenticado.
    """
    result = await session.execute(select(User))
    users = result.scalars().all()
    return {'userlist': users}


@router.get(
    '/own_profile',
    response_model=ProfilePublic,
    status_code=HTTPStatus.OK,
    summary='Retorna próprio perfil',
    description='Retorna o próprio perfil do usuário com informações públicas',
)
async def get_profile(session: SessionDep, current_user: DepCurrentUser):
    query = select(Profile).where(Profile.user_id == current_user.id)
    profile = await session.scalar(query)
    return profile


@router.patch(
    '/own_profile/update',
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
    try:
        update_data = profile_data.model_dump(exclude_unset=True)
        profile_db.sqlmodel_update(update_data)
        session.add(profile_db)
        await session.commit()
        await session.refresh(profile_db)
        return profile_db
    except IntegrityError as e:
        await session.rollback()
        er_msg = str(e.orig).lower()
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail=f'Integrity Error: {er_msg}'
        )
    except Exception:
        await session.rollback()
        raise HTTPException()
