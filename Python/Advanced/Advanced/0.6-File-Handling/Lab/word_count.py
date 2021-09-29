import re
from os import path


def create_input_file(input_file):
    with open(input_file, 'w') as file:
        line = input()
        while line:
            file.write(f"{line}\n")
            line = input()


def find_existing_words(searched_words_file, input_file):
    with open(searched_words_file, 'r') as file:
        searched_words = file.readline().split()

    words_dict = {}
    for word in searched_words:
        pattern = re.compile(fr"^|(?<=[^A-Za-z\d])({word})", re.IGNORECASE)
        if word not in words_dict:
            words_dict[word] = 0

        with open(input_file, 'r') as file:
            for line in file:
                found_words = [w for w in re.findall(pattern, line) if w]
                words_dict[word] += len(found_words)

    return words_dict


def create_output_file(output_file, words):
    with open(output_file, 'w') as file:
        for word, count in sorted(words.items(), key=lambda x: -x[1]):
            file.write(f"{word} - {count}\n")


def read_output_file(output_file):
    with open(output_file, 'r') as file:
        return '\n'.join([f"{line[:-1]}" for line in file if line])


current_dir_path = path.dirname(path.abspath(__file__))
input_file_path = path.join(current_dir_path, 'Files', 'input.txt')
searched_words_file_path = path.join(current_dir_path, 'Files', 'words.txt')
output_file_path = path.join(current_dir_path, 'Files', 'output.txt')

create_input_file(input_file_path)
words_data = find_existing_words(searched_words_file_path, input_file_path)
create_output_file(output_file_path, words_data)
print(read_output_file(output_file_path))
