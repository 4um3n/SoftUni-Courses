import os
import re

input_file_path = os.path.join(os.getcwd(), 'Files', 'text.txt')
output_file_path = os.path.join(os.getcwd(), 'Files', 'output.txt')
letters_pattern = r"[A-Za-z\d]"
symbols_pattern = r"[^A-Za-z\d\s]"

with open(input_file_path, 'r') as file:
    lines = file.read().split('\n')
    
    for i in range(len(lines)):
        letters_count = len([w for w in re.findall(letters_pattern, lines[i]) if w])
        symbols_count = len([s for s in re.findall(symbols_pattern, lines[i]) if s])
        lines[i] = f"Line {i+1}: {lines[i]}({letters_count})({symbols_count})"

with open(output_file_path, 'w') as file:
    file.write('\n'.join(lines))
