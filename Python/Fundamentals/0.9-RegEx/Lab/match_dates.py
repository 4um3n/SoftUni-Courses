import re

pattern = r"(\d{2})(/|\.|-)([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, input())
matches = [f"Day: {m[0]}, Month: {m[2]}, Year: {m[3]}" for m in matches]
print('\n'.join(matches))
