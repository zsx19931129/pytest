# content of test_mark_classlevel.py
import pytest

pytestmark = pytest.mark.webtest

@pytest.mark.webtest
class TestClass:
	pytestmark = [pytest.mark.webtest, pytest.mark.slowtest]
    def test_startup(self):
        pass
    def test_startup_and_more(self):
        pass