# content of tests/test_something_else.py
import pytest

@pytest.fixture
def username(username):
    return 'overridden-else-' + username

def test_username(username):
    assert username == 'overridden-else-username'