# content of tests/test_something.py
import pytest

@pytest.fixture
def username(username):
    return 'overridden-' + username

def test_username(username):
    assert username == 'overridden-username'