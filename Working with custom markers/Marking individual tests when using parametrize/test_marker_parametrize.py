import pytest

@pytest.mark.foo
@pytest.mark.parametrize(("n", "expected"), [
    (1, 2),
    pytest.mark.bar((1, 3)),
    (2, 3),
])
def test_increment(n, expected):
     assert n + 1 == expected