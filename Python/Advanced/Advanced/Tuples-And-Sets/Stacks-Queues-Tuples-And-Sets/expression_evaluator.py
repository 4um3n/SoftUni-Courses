from collections import deque

expression = deque(input().split())
control = deque()
while expression:
    try:
        char = int(expression[0])
        expression.popleft()
        control.append(char)
        continue
    except ValueError:
        char = expression.popleft()

    n = control.popleft()
    while control:
        if char == "*":
            n *= control.popleft()
        elif char == "-":
            n -= control.popleft()
        elif char == "+":
            n += control.popleft()
        elif char == "/":
            n = n // control.popleft()

    control.append(n)

print(*control)
