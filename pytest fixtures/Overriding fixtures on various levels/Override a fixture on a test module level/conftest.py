# content of tests/conftest.py
import pytest

@pytest.fixture
def username():
    return 'username'