import os
from os import path

current_dir_path = path.dirname(path.abspath(__file__))
path = path.join(current_dir_path, 'Files', 'my_first_file.txt')
try:
    os.remove(path)
except FileNotFoundError:
    print(f"File already deleted!")
