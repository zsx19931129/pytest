# content of a/conftest.py
import pytest

class DB:
    pass

@pytest.fixture(scope="session")
def db():
    return DB()
