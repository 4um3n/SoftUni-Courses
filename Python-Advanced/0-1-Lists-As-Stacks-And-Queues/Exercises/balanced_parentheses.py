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


'''

from collections import deque


def is_parentheses_balanced(parentheses, possible_parentheses, opened_i=deque(), i=0):
    if i == len(parentheses):
        if opened_i:
            return "NO"
        return "YES"

    if parentheses[i] in possible_parentheses.keys():
        opened_i.append(i)
    elif parentheses[i] in possible_parentheses.values():
        open_i = opened_i.pop() if opened_i else None
        if open_i is None or parentheses[i] != possible_parentheses[parentheses[open_i]]:
            print("NO")
            exit()

    return is_parentheses_balanced(parentheses, possible_parentheses, opened_i, i+1)


parentheses_data = input()
parentheses_dict = {"{": "}", "[": "]", "(": ")"}
print(is_parentheses_balanced(parentheses_data, parentheses_dict))

'''
