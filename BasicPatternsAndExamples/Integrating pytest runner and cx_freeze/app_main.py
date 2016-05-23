# contents of app_main.py
import sys

if len(sys.argv) > 1 and sys.argv[1] == '--pytest':
    import pytest
    sys.exit(pytest.main(sys.argv[2:]))
else:
    # normal application execution: at this point argv can be parsed
    # by your argument-parsing library of choice as usual
    # ...
    # ./app_main --pytest --verbose --tb=long --junitxml=results.xml test-suite/