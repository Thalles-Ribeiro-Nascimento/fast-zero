from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """
    3 Etapas (AAA):
    A: Arrange - Arranjo: Configuração do que é necessário
    A: Act - Executa o SUT (System Under Test)
    A: Assert - Garante que algo é algo = resposta correta
    :return:
    """
    # Arranjo
    client = TestClient(app)

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá, mundo!"}
