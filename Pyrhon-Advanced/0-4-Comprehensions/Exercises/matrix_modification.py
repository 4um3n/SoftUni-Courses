matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
data = input()
while data != "END":
    data = data.split()
    command = data.pop(0)
    row, col, val = [int(n) for n in data]
    if row in range(len(matrix)) and col in range(len(matrix[row])):
        if command == "Add":
            matrix[row][col] += val
        elif command == "Subtract":
            matrix[row][col] -= val
    else:
        print(f"Invalid coordinates")

    data = input()

[print(*matrix[r]) for r in range(len(matrix))]
