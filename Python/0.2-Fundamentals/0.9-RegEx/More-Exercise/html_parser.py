import re

title_pattern = r"<title>(.*)</title>"
content_pattern = r"<body>(.*)</body>"
tags_pattern = r"(^|(?<=\s)|(?<=>)|(?<=\\n))([\w\d\!\?\.-]+)($|(?=<)|(?=\s)|(?=\\n))"
text = input()
title = ''.join(re.findall(title_pattern, text))
content = ''.join(re.findall(content_pattern, text))
title = ' '.join([g.group() for g in re.finditer(tags_pattern, title)])
content = ' '.join([g.group() for g in re.finditer(tags_pattern, content)])
print(f"Title: {title}")
print(f"Content: {content}")
