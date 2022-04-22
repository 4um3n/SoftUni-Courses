rows, cols = input().split(", ")
matrix = [[int(n) for n in input().split(", ")] for _ in range(int(rows))]
print(sum([n for i in range(len(matrix)) for n in matrix[i]]))
print(matrix)
