# content of conftest.py
import sys

def pytest_runtest_setup(item):
    g = item.get_marker("glob")
    if g is not None:
        for info in g:
            print ("glob args=%s kwargs=%s" %(info.args, info.kwargs))
            sys.stdout.flush()