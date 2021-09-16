n = int(input())
grid = [[int(el) for el in input().split()] for _ in range(n)]
diagonal1_sum = sum([grid[r][r] for r in range(len(grid))])
print(diagonal1_sum)
