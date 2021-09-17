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

    r1, c1, r2, c2 = [int(n) for n in data]
    if r1 not in range(len(matrix)) or r2 not in range(len(matrix)) \
             or c1 not in range(len(matrix[r1])) or c2 not in range(len(matrix[r2])):
        print(f"Invalid input!")
    else:
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(' '.join(matrix[r])) for r in range(len(matrix))]

    data = input()
