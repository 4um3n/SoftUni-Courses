matrix = [[int(n) for n in input().split(", ")] for _ in range(int(input()))]
print([n for i in range(len(matrix)) for n in matrix[i]])
