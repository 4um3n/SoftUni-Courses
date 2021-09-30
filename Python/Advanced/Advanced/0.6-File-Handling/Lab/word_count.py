import re
from os import path


def find_existing_words(searched_words_file, input_file):
    with open(searched_words_file, 'r') as file:
        searched_words = file.read().split()

    occurrences = {}
    for word in searched_words:
        pattern = re.compile(fr"^|(?<=[^A-Za-z\d])({word})(?=[^A-Za-z\d])|$", re.IGNORECASE)
        if word not in occurrences:
            occurrences[word] = 0

        with open(input_file, 'r') as file:
            for line in file:
                found_words = [w for w in re.findall(pattern, line) if w]
                occurrences[word] += len(found_words)

    return occurrences


def create_output_file(output_file, words):
    with open(output_file, 'w') as file:
        for word, count in sorted(words.items(), key=lambda x: -x[1]):
            file.write(f"{word} - {count}\n")


def read_output_file(output_file):
    with open(output_file, 'r') as file:
        return '\n'.join([line[:-1] for line in file if line])


current_dir_path = path.dirname(path.abspath(__file__))
input_file_path = path.join(current_dir_path, 'Files', 'input.txt')
searched_words_file_path = path.join(current_dir_path, 'Files', 'words.txt')
output_file_path = path.join(current_dir_path, 'Files', 'output.txt')

words_data = find_existing_words(searched_words_file_path, input_file_path)
create_output_file(output_file_path, words_data)
print(read_output_file(output_file_path))
