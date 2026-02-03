from fastapi import APIRouter

from ..schemas import User, UserInput, UserPublic, UserPublicList

db = []

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.post(
    '/create',
    response_model=UserPublic,
)
def create_user(user_input: UserInput):
    new_id = len(db) + 1
    user_data = user_input.model_dump()
    new_user = User(**user_data, id=new_id)
    db.append(new_user)

    return new_user


@router.get('/list', response_model=UserPublicList)
def list_users():
    return {'publiclist': db}
