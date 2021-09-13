from collections import deque

parentheses_data = input()
parentheses_dict = {"{": "}", "[": "]", "(": ")"}
opening_indexes = deque()
for i in range(len(parentheses_data)):
    if parentheses_data[i] in parentheses_dict.keys():
        opening_indexes.append(i)
    elif parentheses_data[i] in parentheses_dict.values():
        open_i = opening_indexes.pop() if opening_indexes else None
        if open_i is None or parentheses_data[i] != parentheses_dict[parentheses_data[open_i]]:
            print("NO")
            exit()

if opening_indexes:
    print("NO")
else:
    print("YES")
