from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from ..database import SessionDep
from ..exceptions import ResponseMessage
from ..models import Friendship, FriendStatus, User
from ..security import DepCurrentUser

router = APIRouter(prefix='/friends', tags=['friends'])


@router.post(
    '/request/{friend_id}',
    status_code=HTTPStatus.CREATED,
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
        raise HTTPException(
            HTTPStatus.NOT_FOUND, detail=ResponseMessage.NOT_FOUND_USER
        )

    # consulta amizades do current user
    # regra de negocio (id menor sempre antes)
    id1, id2 = sorted([current_user.id, friend_id])
    query = select(Friendship).where(
        (Friendship.user_id1 == id1) & (Friendship.user_id2 == id2)
    )
    friendship = await session.scalar(query)

    # verifica se ja eh amigo do friend_id (aceito, pendente ou bloqueado)
    if friendship:
        if friendship.status == FriendStatus.ACCEPTED:
            raise HTTPException(HTTPStatus.CONFLICT, detail='Already friends')
        if friendship.status == FriendStatus.PENDING:
            raise HTTPException(
                HTTPStatus.CONFLICT, detail='Request already pending'
            )
        if friendship.status == FriendStatus.BLOCKED:
            if friendship.requested_by == friend_id:
                raise HTTPException(
                    HTTPStatus.FORBIDDEN,
                    detail='This user blocked you or vice versa',
                )

    # caso passe manda requisicao
    new_request = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=current_user.id,
        status=FriendStatus.PENDING,
    )
    try:
        session.add(new_request)
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail='Friend request already exists'
        )
    except Exception:
        await session.rollback()
        raise HTTPException(HTTPStatus.INTERNAL_SERVER_ERROR)

    return {'message': 'Requested successfully!'}
