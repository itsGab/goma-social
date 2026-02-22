from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from ..database import SessionDep
from ..exceptions import (
    HTTPException,
    ResponseMessage,
)
from ..models import (
    ErrorMessage,
    Friendship,
    FriendStatus,
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
    responses={HTTPStatus.CONFLICT: {'model': ErrorMessage}},
)
async def create_user(user_input: UserInput, session: SessionDep):
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
    except Exception:
        await session.rollback()
        raise HTTPException(
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )


@router.get(
    '/list',
    response_model=UserList,
    status_code=HTTPStatus.OK,
    summary='Lista usuários',
    description='Faz a listagem de usuários com informações públicas.',
)
async def list_users(session: SessionDep, current_user: DepCurrentUser):
    """
    Lista os usuários (Requer autenticação)
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
    query = select(Profile).where(
        Profile.user_id == current_user.id  # type: ignore
    )
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
    if not profile_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=ResponseMessage.NOT_FOUND_USER,
        )
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
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR)


@router.post(
    '/friend_request/{friend_id}',
)
async def friend_request(
    friend_id: int, session: SessionDep, current_user: DepCurrentUser
):
    # verifica se current user tem id
    if current_user.id == friend_id:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail="You can't be friends with yourself"
        )

    # verifca se amigo existe
    friend = await session.get(User, friend_id)
    if not friend:
        HTTPException(
            HTTPException.NOT_FOUND, detail=ResponseMessage.NOT_FOUND_USER
        )

    # consulta amizades do current user
    query = select(Friendship).where(
        (
            (Friendship.user_id_1 == current_user.id)
            & (Friendship.user_id_2 == friend_id)
        )
        | (
            (Friendship.user_id_2 == current_user.id)
            & (Friendship.user_id_1 == friend_id)
        )
    )
    friends_db = await session.scalar(query)

    # verifica se ja eh amigo do friend_id (aceito, pendente ou bloqueado)
    if friends_db:
        if friends_db.status == FriendStatus.ACCEPTED:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST, detail='Already friends'
            )
        if friends_db.status == FriendStatus.PENDING:
            raise HTTPException(
                HTTPStatus.BAD_REQUEST, detail='Request already pending'
            )
        if friends_db.status == FriendStatus.BLOCKED:
            raise HTTPException(
                HTTPStatus.FORBIDDEN,
                detail='This user blocked you or vice versa',
            )

    # caso passe manda requisicao
    new_request = Friendship(
        user_id_1=current_user.id,
        user_id_2=friend_id,
    )
    session.add(new_request)
    await session.commit()

    return {'message': 'solicitacao enviada'}
