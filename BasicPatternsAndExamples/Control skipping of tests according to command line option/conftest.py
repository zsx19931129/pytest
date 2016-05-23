# Here is a conftest.py file adding a --runslow command line 
# option to control skipping of slow marked tests:

# content of conftest.py

import pytest
def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", help="run slow tests")




