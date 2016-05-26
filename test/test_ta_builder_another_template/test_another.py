
def test_another_A(request, fixA):
	print 'in test_another_A %s %s %s' % (fixA["uri"], fixA["user"], fixA["password"])
	fixA["password"] = "helloworld_another"
