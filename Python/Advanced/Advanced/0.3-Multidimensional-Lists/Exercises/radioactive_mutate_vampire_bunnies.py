from collections import deque


def find_player(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "P":
                return r, c


def find_bunnies(field):
    bunnies = [(r, c) for r in range(len(field)) for c in range(len(field[r])) if field[r][c] == "B"]
    return bunnies


def spread_bunnies(bunnies, field):
    for r, c in bunnies:
        if r-1 in range(len(field)):
            field[r-1][c] = "B"
        if r+1 in range(len(field)):
            field[r+1][c] = "B"
        if c-1 in range(len(field[0])):
            field[r][c-1] = "B"
        if c+1 in range(len(field[0])):
            field[r][c+1] = "B"

    return field


def play(field, commands):
    while commands:
        direction = commands.popleft()
        r, c = find_player(field)
        field[r][c] = "."
        if direction == "U" and r - 1 in range(len(field)):
            r -= 1
        elif direction == "D" and r + 1 in range(len(field)):
            r += 1
        elif direction == "L" and c - 1 in range(len(field[0])):
            c -= 1
        elif direction == "R" and c + 1 in range(len(field[0])):
            c += 1
        else:
            field = spread_bunnies(find_bunnies(field), field)
            [print(''.join(field[r])) for r in range(len(field))]
            return f"won: {r} {c}"

        field = spread_bunnies(find_bunnies(field), field)
        if field[r][c] == "B":
            [print(''.join(field[r])) for r in range(len(field))]
            return f"dead: {r} {c}"
        else:
            field[r][c] = "P"


rows, cols = [int(n) for n in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands_data = deque(input())
print(play(matrix, commands_data))
