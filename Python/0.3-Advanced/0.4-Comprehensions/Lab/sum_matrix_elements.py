rows, cols = [int(n) for n in input().split(", ")]
matrix = [[int(n) for n in input().split(", ")] for _ in range(rows)]
print(sum([sum(matrix[r]) for r in range(len(matrix))]))
print(matrix)
