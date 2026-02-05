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
    # client = TestClient(app)

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
