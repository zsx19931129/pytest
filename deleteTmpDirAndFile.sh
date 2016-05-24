#! /bin/bash

find . -type d -name "__pycache__" | xargs -I {} echo \"{}\" | xargs rm -rf
find . -type d -name ".cache" | xargs -I {} echo \"{}\" | xargs rm -rf
find . -name "*.pyc" | xargs -I {} echo \"{}\" | xargs rm -rf
