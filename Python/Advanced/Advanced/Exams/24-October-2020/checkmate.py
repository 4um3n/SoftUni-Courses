def find_king(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "K":
                return r, c


def check_direction(field, direction, r, c):
    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1
    elif direction == "up_left":
        r, c = r-1, c-1
    elif direction == "up_right":
        r, c = r-1, c+1
    elif direction == "down_left":
        r, c = r+1, c-1
    elif direction == "down_right":
        r, c = r+1, c+1

    if r not in range(len(field)) or c not in range(len(field[r])):
        return None, None

    elif field[r][c] == "Q":
        return r, c

    return check_direction(field, direction, r, c)


def play(field, directions, r, c, annoyed_queens=[]):
    if not directions:
        if not annoyed_queens:
            return f"The king is safe!"
        return '\n'.join(str(data) for data in annoyed_queens)

    qr, qc = check_direction(field, directions[0], r, c)
    if qr is not None and qc is not None:
        annoyed_queens.append([qr, qc])

    return play(field, directions[1:], r, c, annoyed_queens)


matrix = [input().split() for _ in range(8)]
possible_directions = ['right', 'left', 'down', 'up', 'up_left', 'down_right', 'up_right', 'down_left']
print(play(matrix, possible_directions, *find_king(matrix)))


'''
. . . . . . . .
Q . . . . . . .
. K . . . Q . .
. . . Q . . . .
Q . . . Q . . .
. Q . . . . . .
. . . . . . Q .
. Q . Q . . . .
'''