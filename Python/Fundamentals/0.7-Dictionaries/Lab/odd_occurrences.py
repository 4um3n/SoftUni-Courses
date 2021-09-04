words = [s.lower() for s in input().split()]
sorted_words = []
for w in words:
    if words.count(w) % 2 == 1 and w not in sorted_words:
        sorted_words.append(w)

print(' '.join(sorted_words))
