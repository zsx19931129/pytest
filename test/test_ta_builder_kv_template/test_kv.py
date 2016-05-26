
def test_kv_A(request, fixA):
	print 'in test_kv_A %s %s %s' % (fixA["uri"], fixA["user"], fixA["password"])
	fixA["password"] = "helloworld_kv"