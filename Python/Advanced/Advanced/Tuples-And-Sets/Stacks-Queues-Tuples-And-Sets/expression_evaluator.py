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
    if char == "*":
        while control:
            n *= control.popleft()

    elif char == "-":
        while control:
            n -= control.popleft()

    elif char == "+":
        while control:
            n += control.popleft()

    elif char == "/":
        while control:
            n = n // control.popleft()

    control.append(n)

print(*control)
