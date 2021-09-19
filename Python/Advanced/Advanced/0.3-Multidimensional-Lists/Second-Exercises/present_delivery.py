def find_santa(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "S":
                return r, c


def move(field, direction):
    r, c = find_santa(field)
    r1, c1 = r, c
    if direction == "up":
        r1 -= 1
    elif direction == "down":
        r1 += 1
    elif direction == "left":
        c1 -= 1
    elif direction == "right":
        c1 += 1

    if r1 in range(len(field)) and c1 in range(len(field[r1])):
        field[r][c] = "-"
        return field, r1, c1

    return field, r, c


def check_house(field, r, c, nice_kids, presents):
    if field[r][c] == "V":
        nice_kids -= 1
        presents -= 1
        field[r][c] = "-"

    elif field[r][c] == "X":
        field[r][c] = "-"

    elif field[r][c] == "C":
        field, nice_kids, presents = cookie_rush(field, r, c, nice_kids, presents)

    field[r][c] = "S"
    return field, nice_kids, presents


def cookie_rush(field, r, c, nice_kids, presents):
    kids = ["V", "X"]
    for r1, c1 in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if field[r1][c1] in kids and presents:
            if field[r1][c1] == "V":
                nice_kids -= 1

            field[r1][c1] = "-"
            presents -= 1

    return field, nice_kids, presents


def play(field, nice_kids, presents):
    direct = input()
    while direct != "Christmas morning":
        field, r, c = move(field, direct)
        field, nice_kids, presents = check_house(field, r, c, nice_kids, presents)
        if not presents:
            if nice_kids:
                print(f"Santa ran out of presents!")
            break

        direct = input()

    return field, nice_kids


presents_count = int(input())
matrix = [input().split() for _ in range(int(input()))]
initial_nice_kids_count = sum([matrix[r].count("V") for r in range(len(matrix))])
matrix, nice_kids_count = play(matrix, initial_nice_kids_count, presents_count)

[print(' '.join(matrix[r])) for r in range(len(matrix))]
if not nice_kids_count:
    print(f"Good job, Santa! {initial_nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
