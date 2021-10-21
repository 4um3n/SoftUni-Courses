import re

line, numbers = input(), []
while line:
    numbers.extend(re.findall(r"\d+", line))
    line = input()

print(*numbers)
