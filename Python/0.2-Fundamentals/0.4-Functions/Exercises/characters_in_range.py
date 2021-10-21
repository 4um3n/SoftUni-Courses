chars_in_range = lambda a, b: ' '.join([chr(i) for i in range(ord(a) + 1, ord(b))])
print(chars_in_range(input(), input()))
