# content of test_someenv.py

import pytest
@pytest.mark.env("stage1")
def test_basic_db_operation():
    pass