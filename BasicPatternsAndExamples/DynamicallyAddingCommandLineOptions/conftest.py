# content of conftest.py
import sys
def pytest_cmdline_preparse(args):
    if 'xdist' in sys.modules: # pytest-xdist plugin
        import multiprocessing
        num = max(multiprocessing.cpu_count() / 2, 1)
        args[:] = ["-n", str(num)] + args