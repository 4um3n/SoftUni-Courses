rows, cols = [int(n) for n in input().split(", ")]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]
columns_sums = [sum([matrix[r][c] for r in range(len(matrix))]) for c in range(len(matrix[0]))]
[print(s) for s in columns_sums]
