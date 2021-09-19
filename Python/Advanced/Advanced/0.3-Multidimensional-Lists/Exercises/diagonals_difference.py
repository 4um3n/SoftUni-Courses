matrix = [[int(n) for n in input().split()] for _ in range(int(input()))]
diagonal1 = [matrix[r][r] for r in range(len(matrix))]
diagonal2 = [matrix[r][len(matrix[r]) - r - 1] for r in range(len(matrix))]
diff = abs(sum(diagonal1) - sum(diagonal2))
print(diff)
