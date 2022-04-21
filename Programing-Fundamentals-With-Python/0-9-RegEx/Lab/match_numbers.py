import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, input())
matches = [m.group() for m in matches]
print(' '.join(matches))
