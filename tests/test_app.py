from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(cliente):
    """
    3 Etapas (AAA):
    A: Arrange - Arranjo: Configuração do que é necessário
    A: Act - Executa o SUT (System Under Test)
    A: Assert - Garante que algo é algo = resposta correta
    :return:
    """
    # Arranjo
    # client = TestClient(app) -> Está sendo feito no script conftest.py

    # Act
    response = cliente.get("/")

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá, mundo!"}


def test_create_user(cliente):

    response = cliente.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(cliente):
    response = cliente.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "usuarios": [
            {
                "username": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_users(cliente):
    response = cliente.put(
        "/users/1",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user(cliente):
    response = cliente.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Usuário Excluído"}
