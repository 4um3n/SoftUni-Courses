import re

pattern = r"\b_([A-Za-z\d]+)\b"
variables = re.findall(pattern, input())
print(','.join(variables))