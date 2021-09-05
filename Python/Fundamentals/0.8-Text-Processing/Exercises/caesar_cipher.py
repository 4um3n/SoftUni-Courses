text = input()
text = ''.join([chr(ord(ch) + 3) for ch in text])
print(text)
