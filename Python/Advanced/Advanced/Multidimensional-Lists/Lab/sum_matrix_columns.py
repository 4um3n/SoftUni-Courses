rows, cols = input().split(", ")
grid = [[int(n) for n in input().split()] for _ in range(int(rows))]
matrix_columns_sums = [str(sum([grid[r][c] for r in range(len(grid))])) for c in range(len(grid[0]))]
print('\n'.join(matrix_columns_sums))
