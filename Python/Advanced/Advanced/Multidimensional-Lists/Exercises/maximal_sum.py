from sys import maxsize

rows, cols = [int(n) for n in input().split()]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]
max_sum = -maxsize
square_rows = []
for r in range(rows - 2):
    for c in range(cols - 2):
        result = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2]
        result += matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2]
        result += matrix[r+2][c] + matrix[r+2][c+1] + matrix[r+2][c+2]

        if result > max_sum:
            max_sum = result
            square_rows.clear()
            square_rows.append([str(matrix[r][c]),  str(matrix[r][c+1]), str(matrix[r][c+2])])
            square_rows.append([str(matrix[r+1][c]),  str(matrix[r+1][c+1]), str(matrix[r+1][c+2])])
            square_rows.append([str(matrix[r+2][c]),  str(matrix[r+2][c+1]), str(matrix[r+2][c+2])])

print(f"Sum = {max_sum}")
for i in range(3):
    print(' '.join(square_rows[i]))
