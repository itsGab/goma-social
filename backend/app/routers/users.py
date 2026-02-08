from fastapi import APIRouter
from sqlalchemy import select

from ..database import SessionDep
from ..exceptions import UserConflictException
from ..models import User, UserInput, UserPublic, UserPublicList
from ..security import DepCurrentUser, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/create', response_model=UserPublic)
async def create_user(user_input: UserInput, session: SessionDep):
    # verifica se existe no banco de dados
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


@router.get('/list', response_model=UserPublicList)
async def list_users(session: SessionDep, current_user: DepCurrentUser):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return {'publiclist': users}
