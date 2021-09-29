def find_bunny(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def collect_eggs(field, direction, r, c):
    moves = []
    possible_directions = {
        "up": lambda row, col: (row-1, col),
        "down": lambda row, col: (row+1, col),
        "left": lambda row, col: (row, col-1),
        "right": lambda row, col: (row, col+1),
    }
    r, c = possible_directions[direction](r, c)
    while r in range(len(field)) and c in range(len(field[r])) and field[r][c] != "X":
        moves.append([r, c])
        r, c = possible_directions[direction](r, c)

    return moves


def play(field, directions):
    max_collected_eggs, direction_to_go, made_moves = 0, "", []
    for direction in directions:
        moves = collect_eggs(field, direction, *find_bunny(matrix))
        collected_eggs = sum([int(field[r][c]) for r, c in moves])

        if collected_eggs >= max_collected_eggs:
            max_collected_eggs = collected_eggs
            direction_to_go = direction
            made_moves = moves.copy()

        moves.clear()

    res = f"{direction_to_go}\n"
    res += '\n'.join([f"{made_moves[r]}" for r in range(len(made_moves))])
    res += f"\n{max_collected_eggs}"
    return res


matrix = [input().split() for _ in range(int(input()))]
possible_moves = ["up", "down", "left", "right"]
print(play(matrix, possible_moves))
