import re

pattern = r"\+359(\s|-)2\1\d{3}\1\d{4}\b"
phones = input()
matched_phones = re.finditer(pattern, phones)
matched_phones = [p.group() for p in matched_phones]
print(', '.join(matched_phones))
