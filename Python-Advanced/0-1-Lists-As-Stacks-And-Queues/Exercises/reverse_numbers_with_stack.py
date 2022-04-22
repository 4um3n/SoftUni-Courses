from collections import deque
numbers = deque(input().split())
reversed_numbers = deque()
while numbers:
    reversed_numbers.append(numbers.pop())

print(' '.join(reversed_numbers))