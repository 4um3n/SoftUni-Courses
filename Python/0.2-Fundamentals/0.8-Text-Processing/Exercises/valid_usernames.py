usernames = input().split(", ")
i = 0
while i < len(usernames):
    if len(usernames[i]) not in range(3, 17):
        usernames.pop(i)
        continue

    u = ''.join(usernames[i].split("-"))
    u = ''.join(u.split("_"))
    if not u.isalnum():
        usernames.pop(i)
        continue

    i += 1

print('\n'.join(usernames))


# import re

# pattern = r"^[\w-]{3,16}$"
# usernames, valid_usernames = input().split(", "), []
# for username in usernames:
#     match = re.findall(pattern, username)
#     valid_usernames.extend(match)

# print('\n'.join(valid_usernames))
