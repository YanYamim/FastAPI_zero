from http import HTTPStatus


def test_read_root_deve_retornar_ok(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'password',
            'email': 'teste@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@test.com',
        'id': 1,
    }


def test_get_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@test.com',
                'id': 1,
            }
        ]
    }

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@test.com',
        'id': 1,
    }

def test_get_user_not_found(client):
    response = client.get('/users/666')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'testeusername2',
            'password': '123',
            'email': 'teste@test.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'testeusername2',
        'email': 'teste@test.com',
        'id': 1,
    }

def test_update_user_erro(client):
    response = client.put(
        '/users/666',
        json = {
            'username': 'testeusername2',
            'password': '123',
            'email': 'teste@test.com',
        }
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}

def test_delete_not_found(client):
    response = client.delete('/users/666')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}