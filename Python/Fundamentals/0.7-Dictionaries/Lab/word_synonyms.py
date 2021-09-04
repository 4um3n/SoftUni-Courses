synonyms = {}
for _ in range(int(input())):
    word, synonym = input(), input()
    if word not in synonyms:
        synonyms[word] = []

    synonyms[word].append(synonym)

for w, s in synonyms.items():
    print(f"{w} - {', '.join(s)}")
