text, chars = input().replace(" ", ""), {}
for ch in text:
    if ch not in chars:
        chars[ch] = 0
    
    chars[ch] += 1 

for ch, c in chars.items():
    print(f"{ch} -> {c}")
