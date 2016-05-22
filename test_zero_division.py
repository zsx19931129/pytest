import pytest

def test_zero_division():
	with pytest.raises(ZeroDivisionError) as excinfo:
		1/0
	assert excinfo.type == 'RuntimeError'

