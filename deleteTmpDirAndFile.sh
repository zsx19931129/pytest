find . -type d -name "__pycache__" | xargs -I {} echo \"{}\" | xargs rm -rf
