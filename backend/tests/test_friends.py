# =============================================================================
#                         cenários de friends
# =============================================================================

from http import HTTPStatus
from unittest.mock import patch

import pytest
from sqlalchemy.exc import IntegrityError
from sqlmodel import select

from app.models import Friendship
from app.schemas import FriendAction, FriendStatus


# endpoint: /friends/request ==================================================
# !. post friend request catch not authenticated
def test_friend_request_fail_not_authenticated(client, user, user2):
    response = client.post(f'/friends/requests/{user2.id}')
    data = response.json()

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert data == {'detail': 'Not authenticated'}


# !. post friend request catch cant friend yourself
def test_friend_request_fail_cant_friend_yourself(
    client, user, user2, access_token
):
    response = client.post(
        f'/friends/requests/{user.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data == {'detail': "Can't be friends with yourself"}


# !. post friend request success
def test_friend_request_success(client, user, user2, access_token):
    response = client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert data == {'message': 'Requested successfully!'}


# !. post friend request catch user not found
def test_friend_request_fail_user_not_found(
    client, session, user, access_token
):
    response = client.post(
        f'/friends/requests/{2}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert data == {'detail': 'User not found'}
    assert response.status_code == HTTPStatus.NOT_FOUND


# !. post friend request catch already friend
def test_friend_request_fail_already_friends(
    client, user, user2, access_token, access_token2
):
    # user1 send request
    client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    # user2 accepts request
    response_accept = client.patch(
        '/friends/requests',
        json={'friend_id': user.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    data_accept = response_accept.json()
    # user1 try request again
    response = client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert data_accept == {'message': 'Friend request accepted!'}
    assert response.status_code == HTTPStatus.CONFLICT
    assert data == {'detail': 'Already friends'}


# !. post friend request catch request pending
def test_friend_request_fail_request_pending(
    client, user, user2, access_token
):
    client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    response = client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.CONFLICT
    assert data == {'detail': 'Request already pending'}


# !. post friend request catch you blocked
@pytest.mark.asyncio
async def test_friend_request_fail_you_blocked(
    session, client, user, user2, access_token
):
    user_block = Friendship(
        user_id1=user.id,
        user_id2=user2.id,
        requested_by=user.id,
        blocked_by=user.id,
        status=FriendStatus.BLOCKED,
    )
    session.add(user_block)
    await session.commit()
    await session.refresh(user_block)
    response = client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': "You've blocked this user"}


# !. post friend request catch you are blocked
def test_friend_request_fail_you_are_blocked(
    client, user, user2, access_token, access_token2
):
    client.patch(
        f'/friends/block/{user.id}',
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    response = client.post(
        f'/friends/requests/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': "You're blocked by this user"}


# !. post friend request catch friend req conflict
@pytest.mark.asyncio
async def test_friend_request_db_conflict_mock(
    client, user, user2, access_token, session
):
    # Simulamos que a verificação inicial passou, mas no commit
    # outro processo inseriu o mesmo registro (Race Condition).

    with patch.object(
        session, 'commit', side_effect=IntegrityError(None, None, Exception())
    ):
        response = client.post(
            f'/friends/requests/{user2.id}',
            headers={'Authorization': f'Bearer {access_token}'},
        )

        data = response.json()
        assert response.status_code == HTTPStatus.CONFLICT
        assert data == {'detail': 'Friend request conflicted!'}


# list -------
@pytest.mark.asyncio
async def test_list_pending_requests_success(
    client, session, user, user2, access_token
):
    # Setup: user2 envia pedido para user1 (o 'user' do access_token)
    new_request = Friendship(
        user_id1=min(user.id, user2.id),
        user_id2=max(user.id, user2.id),
        requested_by=user2.id,
        status=FriendStatus.PENDING,
    )
    session.add(new_request)
    await session.commit()

    response = client.get(
        '/friends/requests',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert len(data['pending']) == 1
    assert data['pending'][0]['friend_user_id'] == user2.id
    assert data['pending'][0]['friend_username'] == user2.username


# !. list pending requests empty
def test_friend_list_pending_requests_empty(client, access_token):
    response = client.get(
        '/friends/requests',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data == {'pending': []}


# block ------
# !. post block success (novo bloqueio)
def test_block_user_success(client, user, user2, access_token):
    response = client.patch(
        f'/friends/block/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()
    assert response.status_code == HTTPStatus.OK
    assert data == {'message': 'User blocked'}


# !. post block friend success (novo bloqueio)
@pytest.mark.asyncio
async def test_block_friend_success(
    client, user, user2, access_token, session
):
    # Setup: Cria uma amizade aceita entre eles primeiro
    id1, id2 = sorted([user.id, user2.id])
    friendship = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=user.id,
        status=FriendStatus.ACCEPTED,
    )
    session.add(friendship)
    await session.commit()
    response = client.patch(
        f'/friends/block/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data == {'message': 'User blocked'}

    await session.refresh(friendship)
    assert friendship.status == FriendStatus.BLOCKED
    assert friendship.blocked_by == user.id


# !. block fail yourself
def test_block_fail_yourself(client, user, access_token):
    response = client.patch(
        f'/friends/block/{user.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data == {'detail': 'You cannot block yourself'}


# !. block fail user not found
def test_block_fail_user_not_found(client, user, access_token):
    response = client.patch(
        f'/friends/block/{3}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'User not found'}


# !. post block fail already blocked
def test_block_already_blocked_fail(client, user2, access_token):
    # Bloqueia a primeira vez
    client.patch(
        f'/friends/block/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    # Tenta bloquear novamente
    response = client.patch(
        f'/friends/block/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': 'This user is already blocked'}


# !. post block fail already blocked
def test_block_already_blocked_you_fail(
    client, user, user2, access_token, access_token2
):
    # Bloqueia a primeira vez
    client.patch(
        f'/friends/block/{user.id}',
        headers={'Authorization': f'Bearer {access_token2}'},
    )

    # Tenta bloquear novamente
    response = client.patch(
        f'/friends/block/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': 'This user blocked you'}


# unblock ----
# !. unblock fail yourself
def test_unblock_fail_yourself(client, user, access_token):
    response = client.patch(
        f'/friends/unblock/{user.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data == {'detail': 'You cannot unblock yourself'}


# !. patch unblock success
@pytest.mark.asyncio
async def test_unblock_user_success(
    client, session, user, user2, access_token
):
    # Setup: Criar um bloqueio manual no banco
    block = Friendship(
        user_id1=min(user.id, user2.id),
        user_id2=max(user.id, user2.id),
        requested_by=user.id,
        blocked_by=user.id,
        status=FriendStatus.BLOCKED,
    )
    session.add(block)
    await session.commit()

    response = client.patch(
        f'/friends/unblock/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data == {
        'message': 'User unblocked successfully! Friendship undone!'
    }


# !. unblock fail user not found
def test_unblock_fail_user_not_found(client, user, access_token):
    response = client.patch(
        f'/friends/unblock/{3}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'User not found'}


# !. patch unblock fail not blocked
def test_unblock_fail_not_blocked(client, user2, access_token):
    response = client.patch(
        f'/friends/unblock/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data == {'detail': 'Relationship not found'}


# !. patch unblock fail you are the one blocked
def test_unblock_fail_you_are_blocked_by_them(
    client, user, user2, access_token, access_token2
):
    # User 2 bloqueia User 1
    client.patch(
        f'/friends/block/{user.id}',
        headers={'Authorization': f'Bearer {access_token2}'},
    )

    # User 1 tenta desbloquear User 2 (Não pode!)
    response = client.patch(
        f'/friends/unblock/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()
    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {
        'detail': 'You cannot unblock this user, this user blocked you'
    }


# !. test unblock fail not blocked
@pytest.mark.asyncio
async def test_unblock_fail_friend_not_blocked(
    client, user, user2, access_token, session
):
    id1, id2 = sorted([user.id, user2.id])
    friendship = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=user.id,
        status=FriendStatus.ACCEPTED,
    )
    session.add(friendship)
    await session.commit()
    response = client.patch(
        f'/friends/unblock/{user2.id}',
        headers={'Authorization': f'Bearer {access_token}'},
    )

    data = response.json()
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert data == {'detail': 'This user is not blocked'}


# respond request ----
# !. patch respond friend request accept success
@pytest.mark.asyncio
async def test_respond_friend_request_accept_success(
    client, user, user2, access_token2, session
):
    # Setup: user1 envia pedido para user2
    id1, id2 = sorted([user.id, user2.id])
    req = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=user.id,
        status=FriendStatus.PENDING,
    )
    session.add(req)
    await session.commit()

    # Action: user2 aceita o pedido
    response = client.patch(
        '/friends/requests',
        json={'friend_id': user.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data == {'message': 'Friend request accepted!'}

    await session.refresh(req)
    assert req.status == FriendStatus.ACCEPTED


# !. patch respond friend request reject success
@pytest.mark.asyncio
async def test_respond_friend_request_reject_success(
    client, user, user2, access_token2, session
):
    # Setup: pedido pendente
    id1, id2 = sorted([user.id, user2.id])
    req = Friendship(
        user_id1=id1,
        user_id2=id2,
        requested_by=user.id,
        status=FriendStatus.PENDING,
    )
    session.add(req)
    await session.commit()

    # Action: user2 rejeita (deleta a linha)
    response = client.patch(
        '/friends/requests',
        json={'friend_id': user.id, 'action': FriendAction.REJECT.value},
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.OK
    assert data == {'message': 'Friend request rejected!'}

    result = await session.scalar(
        select(Friendship).where(
            Friendship.user_id1 == id1, Friendship.user_id2 == id2
        )
    )
    assert result is None


# !. patch respond friend request catch not found
def test_respond_friend_request_fail_not_found(client, user2, access_token):
    response = client.patch(
        '/friends/requests',
        json={'friend_id': user2.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert data == {'detail': 'Friend request not found'}


# !. patch respond friend request catch own request
@pytest.mark.asyncio
async def test_respond_friend_request_fail_own_request(
    client, user, user2, access_token, session
):
    id1, id2 = sorted([user.id, user2.id])
    session.add(
        Friendship(
            user_id1=id1,
            user_id2=id2,
            requested_by=user.id,
            status=FriendStatus.PENDING,
        )
    )
    await session.commit()

    # User1 tenta aceitar o pedido que ele mesmo enviou
    response = client.patch(
        '/friends/requests',
        json={'friend_id': user2.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': 'You cannot respond request: Your own request'}


# !. patch respond friend request catch status blocked
@pytest.mark.asyncio
async def test_respond_friend_request_fail_blocked(
    client, user, user2, access_token2, session
):
    id1, id2 = sorted([user.id, user2.id])
    session.add(
        Friendship(
            user_id1=id1,
            user_id2=id2,
            requested_by=user.id,
            blocked_by=user.id,
            status=FriendStatus.BLOCKED,
        )
    )
    await session.commit()

    response = client.patch(
        '/friends/requests',
        json={'friend_id': user.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert data == {'detail': 'You cannot respond request: Status blocked'}


# !. patch respond friend request catch already friends
@pytest.mark.asyncio
async def test_respond_friend_request_fail_already_friends(
    client, user, user2, access_token2, session
):
    id1, id2 = sorted([user.id, user2.id])
    session.add(
        Friendship(
            user_id1=id1,
            user_id2=id2,
            requested_by=user.id,
            status=FriendStatus.ACCEPTED,
        )
    )
    await session.commit()

    response = client.patch(
        '/friends/requests',
        json={'friend_id': user.id, 'action': FriendAction.ACCEPT.value},
        headers={'Authorization': f'Bearer {access_token2}'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.CONFLICT
    assert data == {
        'detail': "You cannot respond request: You're already friends"
    }
