from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select

from ..database import SessionDep
from ..exceptions import UnauthorizedException, UserConflictException
from ..models import ErrorMessage, User, UserInput, UserList, UserPublic
from ..security import DepCurrentUser, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    path='/create',
    response_model=UserPublic,
    status_code=HTTPStatus.CREATED,
    summary='Cria usuário',
    description='Cria um usuario com username, email e password e salva no '
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

    Raises:
        UserConflictException: Se username ou email já constarem na base.
    """
    query = select(User).where(
        (User.username == user_input.username)
        | (User.email == user_input.email)
    )
    db_user = await session.scalar(query)
    if db_user:
        raise UserConflictException()
    user_data = user_input.model_dump()
    hashed_password = get_password_hash(user_data['password'])
    user_data['password'] = hashed_password

    db_user = User(**user_data)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


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
