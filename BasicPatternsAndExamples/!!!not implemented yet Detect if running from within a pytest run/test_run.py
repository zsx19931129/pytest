import sys

def test_runsth():
	if hasattr(sys, '_called_from_test'):
	    # called from within a test run
	    print ('from test')
	else:
	    # called "normally"
	    print ('from normally')