def calculate_number(field, r, c):
    res = 0
    for r1, c1 in ((r-1, c), (r+1, c), (r, c-1), (r, c+1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)):
        if r1 in range(len(field)) and c1 in range(len(field[r1])) and field[r1][c1] == "*":
            res += 1
    return res


def place_numbers(field):
    for r in range(len(field)):
        for c in range(len(field)):
            if field[r][c] == ".":
                res = calculate_number(field, r, c)
                field[r][c] = str(res)
    return field


rows_count, bobs_count = int(input()), int(input())
bombs_positions = [[int(n) for n in input()[1:-1].split(", ")] for _ in range(bobs_count)]
matrix = [["*" if [r, c] in bombs_positions else "." for c in range(rows_count)] for r in range(rows_count)]
matrix = place_numbers(matrix)
[print(' '.join(matrix[r])) for r in range(len(matrix))]
