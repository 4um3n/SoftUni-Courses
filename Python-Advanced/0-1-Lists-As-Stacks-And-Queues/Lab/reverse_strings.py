from collections import deque

text = deque(input())
reversed_text = deque()
while text:
    reversed_text.append(text.pop())

print(''.join(reversed_text))
