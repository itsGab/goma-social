from fastapi import APIRouter
from sqlalchemy import select

from ..database import SessionDep
from ..models import User, UserInput, UserPublic, UserPublicList

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.post('/create', response_model=UserPublic)
async def create_user(user_input: UserInput, session: SessionDep):
    db_user = User.model_validate(user_input)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


@router.get('/list', response_model=UserPublicList)
async def list_users(session: SessionDep):
    result = await session.execute(select(User))
    users = result.scalars().all()
    return {'publiclist': users}
