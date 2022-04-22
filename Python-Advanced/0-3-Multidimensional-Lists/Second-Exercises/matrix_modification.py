from collections import deque

matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
data = input()
while data != "END":
    data = deque(data.split())
    command = data.popleft()
    r, c, val = [int(n) for n in data]
    if r not in range(len(matrix)) or c not in range(len(matrix[r])):
        print(f"Invalid coordinates")
        data = input()
        continue

    if command == "Add":
        matrix[r][c] += val
    elif command == "Subtract":
        matrix[r][c] -= val

    data = input()

[print(' '.join([str(n) for n in matrix[r]])) for r in range(len(matrix))]
