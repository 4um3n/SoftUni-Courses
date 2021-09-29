def check_kills_count(field, r, c):
    kills_count = 0
    moves = [
        (r-2, c-1),
        (r-2, c+1),
        (r+2, c-1),
        (r+2, c+1),
        (r-1, c-2),
        (r-1, c+2),
        (r+1, c-2),
        (r+1, c+2)
    ]
    for r, c in moves:
        if r in range(len(matrix)) and c in range(len(matrix[r])) and field[r][c] == "K":
            kills_count += 1

    return kills_count


def check_knight_with_max_kills(field):
    kills_count = 0
    r1, c1 = None, None
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "K":
                current_kills = check_kills_count(field, r, c)
                if current_kills > kills_count:
                    kills_count = current_kills
                    r1, c1 = r, c

    return r1, c1


def game(field):
    killed_knights = 0
    r, c = check_knight_with_max_kills(field)
    while r is not None and c is not None:
        field[r][c] = 0
        killed_knights += 1
        r, c = check_knight_with_max_kills(field)

    return killed_knights


matrix = [list(input()) for _ in range(int(input()))]
print(game(matrix))
