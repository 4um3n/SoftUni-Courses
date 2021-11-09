def reverse_text(text: str):
    index = len(text) - 1
    while index > -1:
        yield text[index]
        index -= 1


test = reverse_text("step")
for char in test:
    print(char, end='')

print()
for char in test:
    print(char, end='')
