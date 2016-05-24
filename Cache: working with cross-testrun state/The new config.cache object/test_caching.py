# content of test_caching.py
import pytest
import time

@pytest.fixture
def mydata(request):
    val = request.config.cache.get("example/value", None)
    if val is None:
        time.sleep(9*0.6) # expensive computation :)
        val = 42
        request.config.cache.set("example/value", val)
    return val

def test_function(mydata):
    assert mydata == 23