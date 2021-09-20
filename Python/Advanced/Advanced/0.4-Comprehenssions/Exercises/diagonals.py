matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
primary_diagonal = [matrix[r][r] for r in range(len(matrix))]
secondary_diagonal = [matrix[r][len(matrix[r]) - r - 1] for r in range(len(matrix))]
print(f"First diagonal: {', '.join([str(n) for n in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Second diagonal: {', '.join([str(n) for n in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
