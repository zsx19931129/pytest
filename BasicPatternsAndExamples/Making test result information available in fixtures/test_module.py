# content of test_module.py

import pytest

@pytest.fixture
def other():
    assert 0
# add an extra fixture to implement setup failure
def test_setup_fails(something, other):
    pass

def test_call_fails(something):
    assert 0

def test_fail2():
    assert 0