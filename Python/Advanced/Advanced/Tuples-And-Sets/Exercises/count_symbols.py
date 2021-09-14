text = tuple(input())
chars = {char: text.count(char) for char in text}
for char, count in sorted(chars.items()):
    print(f"{char}: {count} time/s")
