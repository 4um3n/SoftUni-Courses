import re

text = input()
pattern = f"\\b{input()}\\b"
matches = re.findall(pattern, text, re.IGNORECASE)
print(len(matches))
