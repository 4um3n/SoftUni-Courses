def find_player(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "P":
                return r, c


def move(field, direction, r, c):
    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1

    return r, c


def play(field, word, r, c, *directions):
    if not directions:
        return f"{word}\n" + '\n'.join([''.join(field[r]) for r in range(len(field))])

    next_r, next_c = move(field, directions[0], r, c)
    if next_r not in range(len(field)) or next_c not in range(len(field[next_r])):
        if word:
            word = word[:-1]
            return play(field, word, r, c, *directions[1:])

    if field[next_r][next_c] != "-":
        word += field[next_r][next_c]

    field[next_r][next_c] = "P"
    field[r][c] = "-"
    return play(field, word, next_r, next_c, *directions[1:])


word_data = input()
matrix = tuple([list(input()) for _ in range(int(input()))])
directions_data = [input() for _ in range(int(input()))]
print(play(matrix, word_data, *find_player(matrix), *directions_data))
