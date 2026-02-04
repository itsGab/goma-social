def test_read_root(client):
    response = client.get('/')
    assert response.json() == {'message': 'Hello from the backend!'}
