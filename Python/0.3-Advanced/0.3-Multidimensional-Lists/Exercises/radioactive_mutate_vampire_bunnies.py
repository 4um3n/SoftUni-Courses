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


def play(field, directions):
    possible_moves = {
        "U": lambda row, col: (row - 1, col),
        "D": lambda row, col: (row + 1, col),
        "L": lambda row, col: (row, col - 1),
        "R": lambda row, col: (row, col + 1),
    }

    while directions:
        direction = directions.popleft()
        r, c = find_player(field)
        field[r][c] = "."
        next_r, next_c = possible_moves[direction](r, c)
        if next_r not in range(len(field)) or next_c not in range(len(field[r])):
            field = spread_bunnies(find_bunnies(field), field)
            res = '\n'.join([''.join(field[r]) for r in range(len(field))])
            res += f"\nwon: {r} {c}"
            return res

        field = spread_bunnies(find_bunnies(field), field)
        if field[next_r][next_c] == "B":
            res = '\n'.join([''.join(field[r]) for r in range(len(field))])
            res += f"\ndead: {next_r} {next_c}"
            return res

        field[next_r][next_c] = "P"


rows, cols = [int(n) for n in input().split()]
matrix = [list(input()) for _ in range(rows)]
commands_data = deque(input())
print(play(matrix, commands_data))
