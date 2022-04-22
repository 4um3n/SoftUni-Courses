from sys import maxsize

rows, cols = [int(n) for n in input().split()]
matrix = [[int(n) for n in input().split()] for _ in range(rows)]
max_sum = -maxsize
square_rows = []
for r in range(rows - 2):
    for c in range(cols - 2):
        current_square = [matrix[r+x][c+y] for x in range(3) for y in range(3)]
        if sum(current_square) > max_sum:
            max_sum = sum(current_square)
            square_rows = current_square.copy()

print(f"Sum = {max_sum}")
square_rows = [[str(square_rows[i]), str(square_rows[i+1]), str(square_rows[i+2])] 
               for i in range(0, len(square_rows), 3)]
[print(' '.join(square_rows[i])) for i in range(3)]
