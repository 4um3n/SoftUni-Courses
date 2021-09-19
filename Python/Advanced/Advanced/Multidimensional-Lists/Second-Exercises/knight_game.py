def check_kills_count(field, r, c):
    kills_count = 0
    for r1 in range(r-2, r+3, 4):
        for c1 in range(c-1, c+2, 2):
            if r1 in range(len(matrix)) and c1 in range(len(matrix[r1])) and field[r1][c1] == "K":
                kills_count += 1

    for r1 in range(r-1, r+2, 2):
        for c1 in range(c-2, c+3, 4):
            if r1 in range(len(matrix)) and c1 in range(len(matrix[r1])) and field[r1][c1] == "K":
                kills_count += 1

    return kills_count


def max_knight_kills(field):
    kills_count = 0
    r1, c1 = None, None
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in range(len(field)) and c in range(len(field[r])) and field[r][c] == "K":
                current_kills = check_kills_count(field, r, c)
                if current_kills > kills_count:
                    kills_count = current_kills
                    r1, c1 = r, c

    return r1, c1


def game(field):
    killed_knights = 0
    r, c = max_knight_kills(field)
    while r is not None and c is not None:
        field[r][c] = 0
        killed_knights += 1
        r, c = max_knight_kills(field)

    return killed_knights


matrix = [list(input()) for _ in range(int(input()))]
print(game(matrix))
