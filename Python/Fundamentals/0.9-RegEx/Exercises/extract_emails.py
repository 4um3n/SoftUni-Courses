import re

pattern = r"(^|(?<=\s))[A-Za-z\d]+([\._-][A-Za-z\d]+)?@[A-Za-z]+(-[A-Za-z]+)?(\.[A-Za-z]+)+"
matches = re.finditer(pattern, input())
matches = [m.group() for m in matches]
print('\n'.join(matches))
