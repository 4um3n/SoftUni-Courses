text = list(input())
strength, i = 0, 0
while i < len(text):
    if text[i] == ">" and i < len(text) - 1:
        i += 1
        strength += int(text[i])
    if strength > 0:
        text.pop(i)
        strength -= 1
        continue
    i += 1

print(''.join(text))
