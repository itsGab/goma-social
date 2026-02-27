from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import or_, select

from ..database import SessionDep
from ..exceptions import ResponseMessage
from ..models import (
    FriendAction,
    FriendRequestPending,
    FriendRequestPublic,
    FriendResponseRequest,
    Friendship,
    FriendStatus,
    RegularMessage,
    User,
)
from ..security import DepCurrentUser

router = APIRouter(prefix='/friends', tags=['friends'])


@router.post(
    '/requests/{friend_id}',
    status_code=HTTPStatus.CREATED,
    response_model=RegularMessage,
)
async def send_friend_request(
    friend_id: int, session: SessionDep, current_user: DepCurrentUser
):
    if current_user.id == friend_id:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, detail="Can't be friends with yourself"
        )

    # regra de negocio (id menor sempre antes)
    id1, id2 = sorted([current_user.id, friend_id])

    new_request = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=current_user.id,
        status=FriendStatus.PENDING,
    )
    session.add(new_request)

    try:
        await session.commit()
        return {'message': 'Requested successfully!'}

    except IntegrityError:
        await session.rollback()

        friend = await session.get(User, friend_id)
        if not friend:
            raise HTTPException(
                HTTPStatus.NOT_FOUND, detail=ResponseMessage.NOT_FOUND_USER
            )

        query = select(Friendship).where(
            Friendship.user_id1 == id1,
            Friendship.user_id2 == id2,
        )
        friendship = await session.scalar(query)
        if friendship:
            if friendship.status == FriendStatus.ACCEPTED:
                raise HTTPException(
                    HTTPStatus.CONFLICT, detail='Already friends'
                )
            if friendship.status == FriendStatus.PENDING:
                raise HTTPException(
                    HTTPStatus.CONFLICT, detail='Request already pending'
                )
            if friendship.status == FriendStatus.BLOCKED:
                if friendship.blocked_by == current_user.id:
                    raise HTTPException(
                        HTTPStatus.FORBIDDEN,
                        detail="You've blocked this user",
                    )
                else:
                    raise HTTPException(
                        HTTPStatus.FORBIDDEN,
                        detail="You're blocked by this user",
                    )

        raise HTTPException(
            HTTPStatus.CONFLICT, detail='Friend request conflicted!'
        )


@router.get('/requests', response_model=FriendRequestPending)
async def list_pending_friend_requests(
    session: SessionDep, current_user: DepCurrentUser
):
    query = (
        select(
            User.id,
            User.username,
            User.email,
            Friendship.status,
            Friendship.created_at,
        )
        .join(Friendship, User)
        .where(
            Friendship.status == FriendStatus.PENDING,
            or_(
                Friendship.user_id1 == current_user.id,
                Friendship.user_id2 == current_user.id,
            ),
            Friendship.requested_by != current_user.id,
        )
        .order_by(Friendship.created_at.asc())
    )
    rows = (await session.execute(query)).mappings().all()

    requests = [
        FriendRequestPublic(
            user_id=row['id'],
            username=row['username'],
            email=row['email'],
            status=row['status'],
            created_at=row['created_at'],
        )
        for row in rows
    ]

    return {'pending': requests}


@router.patch('/requests', response_model=RegularMessage)
async def respond_friend_request(
    response: FriendResponseRequest,
    session: SessionDep,
    current_user: DepCurrentUser,
):
    # regra de negocio (id: A < B)
    id1, id2 = sorted([current_user.id, response.friend_id])

    query = select(Friendship).where(
        Friendship.user_id1 == id1,
        Friendship.user_id2 == id2,
    )
    friendship = await session.scalar(query)

    if not friendship:
        raise HTTPException(
            HTTPStatus.NOT_FOUND, detail='Friend request not found'
        )
    if friendship.status != FriendStatus.PENDING:
        if friendship.status == FriendStatus.BLOCKED:
            raise HTTPException(
                HTTPStatus.FORBIDDEN,
                detail='You cannot respond request: Status blocked',
            )
        if friendship.status == FriendStatus.ACCEPTED:
            raise HTTPException(
                HTTPStatus.CONFLICT,
                detail="You cannot respond request: You're already friends",
            )

    if friendship.requested_by == current_user.id:
        raise HTTPException(
            HTTPStatus.FORBIDDEN,
            detail='You cannot respond request: Your own request',
        )

    if response.action == FriendAction.ACCEPT:
        friendship.status = FriendStatus.ACCEPTED
        await session.commit()
        return {'message': 'Friend request accepted!'}

    elif response.action == FriendAction.REJECT:
        await session.delete(friendship)
        await session.commit()
        return {'message': 'Friend request rejected!'}


@router.patch('/block/{user_id}')
async def block_user(
    user_id: int, session: SessionDep, current_user: DepCurrentUser
):
    # TODO: APLICAR ESSE FUNCAO

    # regra de id
    id1, id2 = sorted([current_user.id, user_id])

    # verifica se usuaria esta bloqueado ou foi bloqueado
    query = select(Friendship).where(
        Friendship.user_id1 == id1,
        Friendship.user_id2 == id2,
        Friendship.blocked_by,
    )

    blocked = await session.scalar(query)

    # levanta erro se sim
    if blocked:
        if blocked.blocked_by == current_user.id:
            raise HTTPException(
                HTTPStatus.FORBIDDEN,
                detail="Cannot block, you've already blocked this user",
            )
        elif blocked.blocked_by == user_id:
            raise HTTPException(
                HTTPStatus.FORBIDDEN,
                detail="Cannot block, you're already blocked by this user",
            )

    # verifica se existe friendship, se nao existe crie e tambem eh o
    query = select(Friendship).where(
        Friendship.user_id1 == id1,
        Friendship.user_id2 == id2,
        Friendship.blocked_by.is_(None),
    )
    do_block = await session.scalar(query)

    # requested_by alem do blocked_by
    if do_block:
        do_block.blocked_by = current_user.id
        do_block.status = FriendStatus.BLOCKED
    else:
        do_block = Friendship(
            user_id1=id1,
            user_id2=id2,
            requested_by=current_user.id,
            blocked_by=current_user.id,
            status=FriendStatus.BLOCKED,
        )
    session.add(do_block)
    await session.commit()

    return {'message': 'User blocked'}


@router.patch('/unblock/{user_id}')
async def unblock_user(
    user_id: int, session: SessionDep, current_user: DepCurrentUser
):
    # TODO: APLICAR ESSE FUNCAO
    # verifica se existe o bloqueio
    # verifica se eh o bloqueador (com permissao para desbloquear)
    # atualiza
    return
