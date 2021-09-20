matrix = [list(input()) for _ in range(int(input()))]
char = input()
chars = [(r, c) for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == char]
print(chars[0]) if chars else print(f"{char} does not occur in the matrix")
