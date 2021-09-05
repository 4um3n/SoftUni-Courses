banned_words = input().split(", ")
text = input()
for ban in banned_words:
    while ban in text:
        text = text.replace(ban, len(ban) * "*")

print(text)
