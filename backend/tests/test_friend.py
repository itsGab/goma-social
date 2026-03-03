# =============================================================================
#                         cenários de friends
# =============================================================================

from http import HTTPStatus


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
# !. post friend request catch already friend
# !. post friend request catch request pending
# !. post friend request catch you blocked
# !. post friend request catch you are blocked
# !. post friend request catch friend req conflict
