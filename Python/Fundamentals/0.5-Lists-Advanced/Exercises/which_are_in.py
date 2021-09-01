substrings = input().split(", ")
strings = input().split(", ")
found_subs = []
for sub in substrings:
    for s in strings:
        if sub in s and sub not in found_subs:
            found_subs.append(sub)

print(found_subs)
