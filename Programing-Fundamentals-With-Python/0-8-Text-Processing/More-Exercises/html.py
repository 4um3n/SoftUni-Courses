title = f"<h1>\n{input()}\n</h1>"
content = f"<article>\n{input()}\n</article>"
comments = []
comment = input()
while comment != "end of comments":
    comments.append(f"<div>\n{comment}\n</div>")
    comment = input()

comments = '\n'.join(comments)
print(f"{title}\n{content}\n{comments}")
