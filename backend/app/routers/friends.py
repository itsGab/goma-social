from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlmodel import select

from ..database import SessionDep
from ..exceptions import ResponseMessage
from ..models import Friendship, FriendStatus, User
from ..security import DepCurrentUser

router = APIRouter(prefix='/friends', tags=['friends'])


@router.post(
    '/request/{friend_id}',
)
async def friend_request(
    friend_id: int, session: SessionDep, current_user: DepCurrentUser
):
    if current_user.id == friend_id:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail="Can't be friends with yourself"
        )

    # verifica se usuario (amigo) existe
    friend = await session.get(User, friend_id)
    if not friend:
        HTTPException(
            HTTPException.NOT_FOUND, detail=ResponseMessage.NOT_FOUND_USER
        )

    # consulta amizades do current user
    # regra de negocio (id menor sempre antes)
    id1, id2 = sorted([current_user.id, friend_id])
    query = select(Friendship).where(
        (Friendship.user_id1 == id1) & (Friendship.user_id2 == id2)
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
    # regra de negocio (id menor sempre antes)
    new_request = Friendship(
        user_id1=id1,
        user_id2=id2,
    )
    session.add(new_request)
    await session.commit()

    return {'message': 'Solicitação enviada!'}
