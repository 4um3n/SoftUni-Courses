rows, cols = [int(n) for n in input().split(", ")]
matrix = [[int(n) for n in input().split(", ")] for _ in range(rows)]
squares = [[matrix[r][c], matrix[r][c+1], matrix[r+1][c], matrix[r+1][c+1]]
           for r in range(len(matrix) - 1)
           for c in range(len(matrix[r]) - 1)]

max_sum = max([sum(squares[r]) for r in range(len(squares))])
print([f"{squares[r][0]} {squares[r][1]} \n{squares[r][2]} {squares[r][3]} " for r in range(len(squares)) if sum(squares[r]) == max_sum][0])
print(max_sum)