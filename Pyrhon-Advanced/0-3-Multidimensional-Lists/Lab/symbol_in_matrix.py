matrix = [list(input()) for _ in range(int(input()))]
symbol = input()
founded = [(r, c) for r in range(len(matrix)) for c in range(len(matrix[r])) if matrix[r][c] == symbol]
if founded:
    print(founded[0])
else:
    print(f"{symbol} does not occur in the matrix")
