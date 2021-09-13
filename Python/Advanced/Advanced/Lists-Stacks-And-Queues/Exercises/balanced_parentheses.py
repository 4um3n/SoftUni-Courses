from collections import deque

parentheses_data = input()
parentheses_dict = {"{": "}", "[": "]", "(": ")"}
open_parentheses, closed_parentheses = [], []
i = 0
while i < len(parentheses_data):
    while i < len(parentheses_data) and parentheses_data[i] in parentheses_dict.keys():
        open_parentheses.append(parentheses_data[i])
        i += 1
    while i < len(parentheses_data) and parentheses_data[i] in parentheses_dict.values():
        closed_parentheses.append(parentheses_data[i])
        i += 1

    closed_parentheses = closed_parentheses[::-1]
    if len(open_parentheses) == len(closed_parentheses):
        for ind in range(len(open_parentheses)):
            if closed_parentheses[ind] != parentheses_dict[open_parentheses[ind]]:
                print("NO")
                exit()

        open_parentheses.clear()
        closed_parentheses.clear()
    else:
        print("NO")
        exit()
        
print("YES")
