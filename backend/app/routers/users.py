from fastapi import APIRouter
from sqlmodel import select

from ..database import SessionDep
from ..models import User, UserInput, UserPublic, UserPublicList

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.post('/create', response_model=UserPublic)
def create_user(user_input: UserInput, session: SessionDep):
    db_user = User.model_validate(user_input)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get('/list', response_model=UserPublicList)
def list_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return {'publiclist': users}
