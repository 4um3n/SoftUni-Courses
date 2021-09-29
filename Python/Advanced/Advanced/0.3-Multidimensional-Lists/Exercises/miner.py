from collections import deque


def find_miner(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "s":
                return r, c


def left_coal(field):
    x = 0
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "c":
                x += 1
    return x


def move(field, directions):
    possible_moves = {
        "up": lambda row, col: (row-1, col),
        "down": lambda row, col: (row+1, col),
        "left": lambda row, col: (row, col-1),
        "right": lambda row, col: (row, col+1),
    }

    while directions:
        direction = directions.popleft()
        r, c = find_miner(field)
        field[r][c] = "*"
        next_r, next_c = possible_moves[direction](r, c)
        if next_r not in range(len(field)) or next_c not in range(len(field[r])):
            field[r][c] = "s"
            continue

        if field[next_r][next_c] == "e":
            return f"Game over! ({next_r}, {next_c})"

        field[next_r][next_c] = "s"
        if not left_coal(field):
            return f"You collected all coal! ({next_r}, {next_c})"

    r, c = find_miner(field)
    remaining_coal = left_coal(field)
    return f"{remaining_coal} pieces of coal left. ({r}, {c})"


rows = int(input())
directions_data = deque(input().split())
matrix = [input().split() for _ in range(rows)]
print(move(matrix, directions_data))
