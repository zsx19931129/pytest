# content of test_myplugin.py

pytest_plugins = "pytester"  # to get testdir fixture

def test_myplugin1(testdir):
    testdir.makepyfile("""
        def test_example():
            pass
    """)
    result = testdir.runpytest("--verbose")
    result.stdout.fnmatch_lines("""
        *test_example*
    """)