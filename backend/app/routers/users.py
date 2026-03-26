from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy.exc import IntegrityError
from sqlmodel import or_, select

from ..database import DepDBSession
from ..exceptions import (
    HTTPException,
    ResponseMessage,
)
from ..models import (
    ErrorMessage,
    RegularMessage,
    User,
    UserInput,
    UserList,
    UserOnDelete,
    UserPublic,
)
from ..security import DepCurrentUser, get_password_hash, verify_password
from .profiles import create_profile

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/create',
    response_model=UserPublic,
    status_code=HTTPStatus.CREATED,
    summary='Cria usuário',
    description='Cria um usuário com username, email e password e salva no '
    'banco de dados.',
    responses={HTTPStatus.CONFLICT: {'model': ErrorMessage}},
)
async def create_user(user_input: UserInput, session: DepDBSession):
    """
    Realiza o cadastro do usuário com hash de senha e validação de duplicidade.
    Cria perfil (profile) para usuário.

    Raises:
        UserConflictException: Se username ou email já constarem na base.
    """
    # verifica conflito com o banco de dados
    query = select(User).where(
        or_(
            User.username == user_input.username,
            User.email == user_input.email,
        )
    )
    db_user = await session.scalar(query)
    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail=ResponseMessage.USER_ANY_CONFLICT,
        )
    # sem conflito, cadastra new user
    hashed_password = get_password_hash(user_input.password)
    new_user = User(
        email=user_input.email,
        username=user_input.username,
        password=hashed_password,
    )
    try:
        session.add(new_user)
        await session.flush()
        await create_profile(new_user, session)
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Integrity Error',
        )

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
    except IntegrityError:
        await session.rollback()
        raise HTTPException(HTTPStatus.BAD_REQUEST, detail='Integrity Error')


@router.get(
    '/list',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    summary='Lista usuários',
    description='Faz a listagem de usuários com informações públicas.',
)
async def list_users(session: DepDBSession, current_user: DepCurrentUser):
    """
    Lista os usuários (Requer autenticação)
    """
    result = await session.execute(select(User))
    users = result.scalars().all()
    return {'userlist': users}
