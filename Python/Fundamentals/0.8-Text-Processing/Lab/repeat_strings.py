words = input().split()
words = [w * len(w) for w in words]
print(''.join(words))