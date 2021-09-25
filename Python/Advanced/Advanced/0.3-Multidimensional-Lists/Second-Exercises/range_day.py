def find_shooter(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "A":
                return r, c


def move(field, direction, steps):
    r, c = find_shooter(field)
    r1, c1 = r, c
    if direction == "right":
        c1 += steps
    elif direction == "left":
        c1 -= steps
    elif direction == "up":
        r1 -= steps
    elif direction == "down":
        r1 += steps

    if r1 in range(len(field)) and c1 in range(len(field[r1])) and field[r1][c1] == ".":
        field[r][c] = "."
        field[r1][c1] = "A"
        return field

    return field


def shoot(field, direction):
    global shoot_targets
    r, c = find_shooter(field)
    while field[r][c] != "x":
        if direction == "right":
            c += 1
        elif direction == "left":
            c -= 1
        elif direction == "up":
            r -= 1
        elif direction == "down":
            r += 1

        if r not in range(len(field)) or c not in range(len(field[r])):
            return field

    shoot_targets.append([r, c])
    field[r][c] = "."
    return field


matrix = [input().split() for _ in range(5)]
targets_count = sum([matrix[r].count("x") for r in range(len(matrix))])
shoot_targets = []
for _ in range(int(input())):
    command = input().split()
    if "move" in command:
        direct, steps_count = command[1], int(command[2])
        matrix = move(matrix, direct, steps_count)
    elif "shoot" in command:
        direct = command[1]
        matrix = shoot(matrix, direct)

    if len(shoot_targets) == targets_count:
        print(f"Training completed! All {targets_count} targets hit.")
        break
else:
    print(f"Training not completed! {targets_count - len(shoot_targets)} targets left.")

[print(shoot_targets[r]) for r in range(len(shoot_targets))]
