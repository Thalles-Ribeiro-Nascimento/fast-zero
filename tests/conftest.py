from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
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


@contextmanager  # Diz para o Python que essa função faz parte de um contexto e pode ser inserido/chamado dentro de um with
def _mock_db_time(*, model, time=datetime(2026, 1, 1)):
    def fake_time_hook(mapper, connection, target):
        if hasattr(target, "created_at"):  # Verifica se o target contém o atributo 'created_at', se existir, insere o Time que foi passado na função _mock_db_time
            target.created_at = time  # Inserindo o time no atributo 'created_at'

        if hasattr(target, "update_at"):
            target.update_at = time

    event.listen(model, "before_insert", fake_time_hook)

    yield time

    event.remove(model, "before_insert", fake_time_hook)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
