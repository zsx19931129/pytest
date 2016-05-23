# contents of setup.py
from cx_Freeze import setup, Executable
import pytest

setup(
    name="app_main",
    executables=[Executable("app_main.py")],
    options={"build_exe":
        {
        'includes': pytest.freeze_includes()}
        },
    # ... other options
)