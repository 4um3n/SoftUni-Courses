matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
print([matrix[r][c] for r in range(len(matrix)) for c in range(len(matrix[r]))])
