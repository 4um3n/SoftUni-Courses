rows, cols = [int(n) for n in input().split()]
matrix = [input().split() for _ in range(rows)]
identical_sub_squares_count = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
            identical_sub_squares_count += 1

print(identical_sub_squares_count)
