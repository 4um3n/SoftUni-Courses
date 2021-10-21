rows, cols = [int(n) for n in input().split()]
matrix = [[f"{chr(let)}{chr(let1)}{chr(let)}" for let1 in range(let, let+cols)] for let in range(ord("a"), ord("a") + rows)]
[print(' '.join(matrix[r])) for r in range(len(matrix))]
