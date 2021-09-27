def find_snake(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "S":
                return r, c


def find_burrow(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def play(field, moves, eaten_food=0):
    if eaten_food == 10:
        res = f"You won! You fed the snake.\n" \
              f"Food eaten: {eaten_food}\n"
        res += '\n'.join([''.join(field[r]) for r in range(len(field))])
        return res

    direction = input()
    r, c = find_snake(field)
    field[r][c] = "."
    next_r, next_c = moves[direction](r, c)
    if next_r not in range(len(field)) or next_c not in range(len(field[next_r])):
        res = f"Game over!\n" \
              f"Food eaten: {eaten_food}\n"
        res += '\n'.join([''.join(field[r]) for r in range(len(field))])
        return res

    if field[next_r][next_c] == "*":
        eaten_food += 1
    elif field[next_r][next_c] == "B":
        field[next_r][next_c] = "."
        next_r, next_c = find_burrow(field)

    field[next_r][next_c] = "S"
    return play(field, moves, eaten_food)


territory = [list(input()) for _ in range(int(input()))]
possible_moves = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1)
}

print(play(territory, possible_moves))
