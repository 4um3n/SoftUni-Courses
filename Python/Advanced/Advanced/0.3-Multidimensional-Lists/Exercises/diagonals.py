matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
diagonal1 = [matrix[r][r] for r in range(len(matrix))]
diagonal2 = [matrix[r][len(matrix[r]) - r - 1] for r in range(len(matrix))]

print(f"Primary diagonal: {', '.join([str(n) for n in diagonal1])}. Sum: {sum(diagonal1)}\n"
      f"Secondary diagonal: {', '.join([str(n) for n in diagonal2])}. Sum: {sum(diagonal2)}")
