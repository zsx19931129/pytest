import pytest

@pytest.fixture
def getFuncargs_Num():
	return 1

class A:
	def hello(self):
		print 'HelloWorld'

@pytest.fixture
def getFuncargs_Class():
	return A()

def tmpFunc():
	print "HelloWorld2"

@pytest.fixture
def getFuncargs_Func():
	return tmpFunc



@pytest.fixture(scope="function")
def setup_function(request):
	def teardown_function():
		print("teardown_function")
	request.addfinalizer(teardown_function)
	print("setup_function called.")

@pytest.fixture(scope="module")
def setup_module(request):
	def teardown_module():
		print("teardown_module called.")
	request.addfinalizer(teardown_module)
	print("setup_module called")

@pytest.fixture(scope="function")
def setup_function_Num(request, getFuncargs_Num):
	def teardown_function():
		print("teardown_function, %d" %getFuncargs_Num)
	request.addfinalizer(teardown_function)
	print("setup_function called. %d" %getFuncargs_Num)

@pytest.fixture(scope="function")
def setup_function_Class(request, getFuncargs_Class):
	def teardown_function():
		print("teardown_function called." )
		getFuncargs_Class.hello()
	request.addfinalizer(teardown_function)
	print("setup_function called.")
	getFuncargs_Class.hello()

@pytest.fixture(scope="function")
def setup_function_Func(request, getFuncargs_Func):
	def teardown_function():
		print("teardown_function called." )
		getFuncargs_Func()
	request.addfinalizer(teardown_function)
	print("setup_function called.")
	getFuncargs_Func()


def test_1(setup_function):
	print("Test_1 called.")

def test_2(setup_module):
	print("Test_2 called.")

def test_3(setup_module):
	print("Test_3 called.")

def test_4(setup_function_Num):
	print("Test_4 called.")

def test_5(setup_function_Class):
	print("Test_5 called.")

def test_6(setup_function_Func):
	print("Test_6 called.")