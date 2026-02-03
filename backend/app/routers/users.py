from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database import get_session
from ..models import User, UserInput, UserPublic, UserPublicList

db = []

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.post(
    '/create',
    response_model=UserPublic,
)
def create_user(
    user_input: UserInput, session: Session = Depends(get_session)
):
    db_user = User.model_validate(user_input)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
    # new_id = len(db) + 1
    # user_data = user_input.model_dump()
    # new_user = User(**user_data, id=new_id)
    # db.append(new_user)

    # return new_user


@router.get('/list', response_model=UserPublicList)
def list_users(session: Session = Depends(get_session)):
    users = session.exec(select(User)).all()
    return {'publiclist': users}
