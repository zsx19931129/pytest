import pytest
import sys
import os.path
import ConfigParser

@pytest.fixture(scope="session")
def fixA(request):
	def setupA():
		print 'In setupA, %s, %s', (request.fixturename, request.scope)
	def teardownA():
		print 'finalvalue: %s %s %s' % (myDict["uri"], myDict["user"], myDict["password"])
		print 'In teardownA, %s, %s', (request.fixturename, request.scope)

	setupA()

	myDict = {}
	myDict["uri"] = "https://127.0.0.1:8089"
	myDict["user"] = "admin"
	myDict["password"] = "changeme"

	trueDict = {}
	curr_path = os.getcwd()
	ini_path = os.path.join(curr_path, "pytest.ini")
	parser = ConfigParser.ConfigParser()
	parser.read(ini_path)
	print parser.sections()
	options = parser.options("splunk_env")
	print options
	for option in options:
		trueDict[option] = parser.get("splunk_env", option)
	for key in trueDict:
		print 'key:%s value:%s' %(key, trueDict[key])
	
	request.addfinalizer(teardownA)
	return myDict
