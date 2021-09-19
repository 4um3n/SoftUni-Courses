def find_bunny(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def move_bunny(field, direction, r, c):
    global current_moves
    if direction == "left":
        c -= 1
    elif direction == "right":
        c += 1
    elif direction == "up":
        r -= 1
    elif direction == "down":
        r += 1

    if r in range(len(field)) and c in range(len(field[r])) and field[r][c] != "X":
        current_moves.append([r, c])
        return move_bunny(field, direction, r, c)

    return 0


matrix = [input().split() for _ in range(int(input()))]
max_collected_eggs = 0
direction_to_go = ""
current_moves, made_moves = [], []
possible_moves = ["up", "down", "left", "right"]
for direct in possible_moves:
    move_bunny(matrix, direct, *find_bunny(matrix))
    collected_eggs = sum([int(matrix[r][c]) for r, c in current_moves])
    if collected_eggs >= max_collected_eggs:
        made_moves = current_moves.copy()
        max_collected_eggs = collected_eggs
        direction_to_go = direct

    current_moves.clear()

print(direction_to_go)
[print(made_moves[r]) for r in range(len(made_moves))]
print(max_collected_eggs)
