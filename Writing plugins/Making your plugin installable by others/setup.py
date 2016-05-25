# sample ./setup.py file
from setuptools import setup

setup(
    name="myproject",
    packages = ['myproject']

    # the following makes a plugin available to pytest
    entry_points = {
        'pytest11': [
            'name_of_plugin = myproject.pluginmodule',
        ]
    },
)