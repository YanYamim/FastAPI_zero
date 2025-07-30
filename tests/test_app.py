from fastapi.testclient import TestClient
from src.fast_zero.app import app
from http import HTTPStatus

def test_read_root_deve_retornar_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}