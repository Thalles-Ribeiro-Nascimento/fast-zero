import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# Princípio DRY - Evitando código Boilerplate
@pytest.fixture
def cliente():
    return TestClient(app)
