sub, text = input(), input()
while sub in text:
    text = text.replace(sub, "")

print(text)