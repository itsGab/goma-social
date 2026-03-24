# =============================================================================
#                         cenários de posts
# =============================================================================

from http import HTTPStatus
from time import sleep


# endpoint: /posts/create =====================================================
# !. create post success
def test_post_create_success(client, user, access_token):
    response = client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do post'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert data['content'] == 'conteudo do post'
    assert data['author'] == {
        'email': user.email,
        'username': user.username,
        'id': user.id,
    }
    assert 'post_id' in data
    assert 'created_at' in data


# !. create post fail not authenticated
def test_post_create_fail_not_authenticated(client, user):
    response = client.post(
        '/posts/create',
        json={'content': 'conteudo do post'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert data == {'detail': 'Not authenticated'}


# endpoint: /posts/my_posts ===================================================
# !. list my posts success
def test_posts_list_my_posts_success(
    client, user, user2, access_token, access_token2
):
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 1'},
    )
    sleep(0.5)
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 2'},
    )
    sleep(0.5)
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 3'},
    )
    sleep(0.5)
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token2}'},
        json={'content': 'conteudo do post de outro usuario'},
    )
    response = client.get(
        '/posts/my_posts',
        headers={'Authorization': f'Bearer {access_token}'},
    )
    data = response.json()
    post_2 = data['posts'][1]
    post_3 = data['posts'][2]
    number_of_posts = 3

    assert response.status_code == HTTPStatus.OK
    assert len(data['posts']) == number_of_posts
    assert post_3['content'] == 'conteudo do meu post 1'
    assert post_3['author']['id'] == user.id
    assert 'post_id' in post_3
    assert 'created_at' in post_3
    assert post_2['created_at'] > post_3['created_at']
    assert 'limit' in data
    assert 'offset' in data
