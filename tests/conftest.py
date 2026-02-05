import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.models import table_registry


# Princípio DRY - Evitando código Boilerplate
@pytest.fixture
def cliente():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")  # Cria o sessão de banco de dados pelo SQLAlchemy
    table_registry.metadata.create_all(engine)  # Cria todas as tabelas necessárias

    with Session(engine) as session:  # Cria uma sessão para que os testes possam se comunicar com o banco de dados via engine
        yield session  # Fornece uma instancia de Session que será injetada em cada teste que solicita a fixture. É utilizada para interagir com o banco

    table_registry.metadata.drop_all(engine)  # Após os testes, dropar todas as tabelas. Isso garante que os testes serão realizados num banco limpo
