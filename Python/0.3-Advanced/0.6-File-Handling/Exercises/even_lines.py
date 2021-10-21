from os import path

current_dir_path = path.dirname(path.abspath(__file__))
file_path = path.join(current_dir_path, 'Files', 'text.txt')
chars_to_replace = ["-", ",", ".", "!", "?"]

with open(file_path, 'r') as file:
    lines = [line for line in file.read().split('\n')]
    lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]

    for i in range(len(lines)):
        line = lines[i]
        for char in chars_to_replace:
            line = line.replace(char, "@", line.count(char))

        lines[i] = ' '.join(line.split()[::-1])

    [print(lines[r]) for r in range(len(lines))]
