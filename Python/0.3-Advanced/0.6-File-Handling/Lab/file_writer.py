from os import path

current_dir_path = path.dirname(path.abspath(__file__))
file_path = path.join(current_dir_path, 'Files', 'my_first_file.txt')
with open(file_path, 'w') as file:
    file.write(f"I just created my first file!")
