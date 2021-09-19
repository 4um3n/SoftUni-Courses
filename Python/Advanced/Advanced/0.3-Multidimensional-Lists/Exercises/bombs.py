matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
bombs_coordinates = [[int(n) for n in c.split(",")] for c in input().split()]
for bomb in bombs_coordinates:
    row, col = bomb
    if matrix[row][col] <= 0:
        continue

    strength = matrix[row][col]
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if r in range(len(matrix)) and c in range(len(matrix[r])) and matrix[r][c] > 0:
                matrix[r][c] -= strength

alive_cells = [matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] > 0]
print(f"Alive cells: {len(alive_cells)}\n"
      f"Sum: {sum(alive_cells)}")

[print(' '.join([str(n) for n in matrix[r]])) for r in range(len(matrix))]
