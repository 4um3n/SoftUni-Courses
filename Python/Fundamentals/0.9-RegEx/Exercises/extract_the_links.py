import re

pattern = r"(^|(?<=\s))www\.[A-Za-z\d-]+(\.[a-z]+)+($|(?=\s))"
line = input()
while line:
    for m in re.finditer(pattern, line):
        print(m.group())

    line = input()
