# content of ./test_parametrize.py
import pytest

def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
            for funcargs in funcarglist])

class TestClass:
    # a map specifying multiple argument sets for a test method
    params = {
        'test_equals': [dict(a=1, b=2), dict(a=3, b=3), ],
        'test_zerodivision': [dict(a=1, b=0), ],
    }

    def test_equals(self, a, b):
        assert a == b

    def test_zerodivision(self, a, b):
        pytest.raises(ZeroDivisionError, "a/b")