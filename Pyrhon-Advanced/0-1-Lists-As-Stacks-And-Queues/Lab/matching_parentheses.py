from collections import deque

text = input()
opening_parentheses = deque()
for i in range(len(text)):
    if text[i] == "(":
        opening_parentheses.append(i)
    elif text[i] == ")":
        start_i = opening_parentheses.pop()
        print(text[start_i:i + 1])

