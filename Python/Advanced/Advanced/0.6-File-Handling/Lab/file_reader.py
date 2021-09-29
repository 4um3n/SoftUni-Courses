from os import path

current_dir_path = path.dirname(path.abspath(__file__))
file_path = path.join(current_dir_path, 'Files', 'text.txt')
with open(file_path, 'r') as file:
    print(sum([int(line) for line in file]))
