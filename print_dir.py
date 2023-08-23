import os

project_dir = "/media/mathieu/Data/code/python/bookscraper"

for root, dirs, files in os.walk(project_dir):
    if "venv" in dirs:
        dirs.remove("venv")
    if "__pycache__" in dirs:
        dirs.remove("__pycache__")
    if ".pytest_cache" in dirs:
        dirs.remove(".pytest_cache")
    if ".git" in dirs:
        dirs.remove(".git")
    
    print(f"Directory: {root}")
    for file in files:
        print(f"  File: {file}")
