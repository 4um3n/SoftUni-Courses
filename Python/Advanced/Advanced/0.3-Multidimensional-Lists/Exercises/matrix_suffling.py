rows, cols = [int(n) for n in input().split()]
matrix = [input().split() for _ in range(rows)]
data = input()
while data != "END":
    data = data.split()
    command = data.pop(0)
    if command != "swap" or len(data) != 4:
        print(f"Invalid input!")
        data = input()
        continue

    values = [(int(data[i]), int(data[i+1])) for i in range(0, len(data), 2)]
    for r, c in values:
        if r not in range(len(matrix)) or c not in range(len(matrix[r])):
            print(f"Invalid input!")
            break
    else:
        r1, c1, r2, c2 = [v for t in values for v in t]
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(' '.join(matrix[r])) for r in range(len(matrix))]

    data = input()
