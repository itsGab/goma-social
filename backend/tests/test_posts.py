from http import HTTPStatus
from time import sleep


# test success post
def test_post_sucess(client, user, access_token):
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


# test fail not authenticated user
def test_post_fail_not_authenticated(client, user):
    response = client.post(
        '/posts/create',
        json={'content': 'conteudo do post'},
    )
    data = response.json()

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert data == {'detail': 'Not authenticated'}


# test success list posts of current user
def test_post_list_success(client, user, user2, access_token, access_token2):
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 1'},
    )
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 2'},
    )
    sleep(1)
    client.post(
        '/posts/create',
        headers={'Authorization': f'Bearer {access_token}'},
        json={'content': 'conteudo do meu post 3'},
    )
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
    assert post_3['content'] == 'conteudo do meu post 3'
    assert post_3['author']['id'] == user.id
    assert 'post_id' in post_3
    assert 'created_at' in post_3
    assert post_2['created_at'] < post_3['created_at']
