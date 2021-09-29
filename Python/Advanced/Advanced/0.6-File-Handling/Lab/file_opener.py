from os import path

current_dir_path = path.dirname(path.abspath(__file__))
file_path = path.join(current_dir_path, 'Files', 'text.txt')
print(f"File{' not' if not path.exists(file_path) else ''} exists")
