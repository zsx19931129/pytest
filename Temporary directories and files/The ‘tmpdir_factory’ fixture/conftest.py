# contents of conftest.py
import pytest

@pytest.fixture(scope='session')
def image_file(tmpdir_factory):
    img = compute_expensive_image()
    fn = tmpdir_factory.mktemp('data').join('img.png')
    img.save(str(fn))
    return fn

# contents of test_image.py
def test_histogram(image_file):
    img = load_image(image_file)
    # compute and test histogram