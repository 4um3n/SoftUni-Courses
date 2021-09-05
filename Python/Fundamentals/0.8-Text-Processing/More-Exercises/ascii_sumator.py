ascii_range = range(ord(input()) + 1, ord(input()))
text_sum = [ord(ch) for ch in input() if ord(ch) in ascii_range]
print(sum(text_sum))
