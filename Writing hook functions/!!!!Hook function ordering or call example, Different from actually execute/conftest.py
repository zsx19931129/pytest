import pytest

# Plugin 1
@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(items):
    # will execute as early as possible
    print 'In plugin 1'

# Plugin 2
@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(items):
    # will execute as late as possible
    print 'In plugin 2'

# Plugin 3
@pytest.hookimpl(hookwrapper=True)
def pytest_collection_modifyitems(items):
    # will execute even before the tryfirst one above!
    print 'In plugin 3 before'
    outcome = yield
    # will execute after all non-hookwrappers executed
    print 'In plugin 3 after'
