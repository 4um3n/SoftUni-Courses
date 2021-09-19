rows, cols = [int(n) for n in input().split()]
snake = tuple(input())
matrix = []
i = 0
for r in range(rows):
    current_row = []
    for c in range(cols):
        current_row.append(snake[i])
        i = 0 if i == len(snake) - 1 else i + 1

    if r % 2 == 1:
        current_row = current_row[::-1]

    matrix.append(current_row)

[print(''.join(matrix[r])) for r in range(len(matrix))]
