# content of conftest.py

import pytest

@pytest.fixture(scope="session")
def basemod(request):
    return pytest.importorskip("base")

@pytest.fixture(scope="session", params=["opt1", "opt2"])
def optmod(request):
    return pytest.importorskip(request.param)