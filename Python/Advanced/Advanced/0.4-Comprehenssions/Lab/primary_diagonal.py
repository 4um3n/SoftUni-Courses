matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
print(sum([matrix[r][r] for r in range(len(matrix))]))
