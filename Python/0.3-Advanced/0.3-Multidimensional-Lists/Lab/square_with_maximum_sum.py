from sys import maxsize

rows, cols = input().split(", ")
matrix = [[int(n) for n in input().split(", ")] for _ in range(int(rows))]
biggest_sum = -maxsize
biggest_row, biggest_col = [], []
for r in range(int(rows) - 1):
    for c in range(int(cols) - 1):
        square_sum = matrix[r][c] + matrix[r][c+1] + matrix[r+1][c] + matrix[r+1][c+1]
        if square_sum > biggest_sum:
            biggest_sum = square_sum
            biggest_row = [matrix[r][c], matrix[r][c+1]]
            biggest_col = [matrix[r+1][c], matrix[r+1][c+1]]

print(*biggest_row)
print(*biggest_col)
print(biggest_sum)
