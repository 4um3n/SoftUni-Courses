from collections import deque


def find_miner(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "s":
                return r, c


def left_coal(grid):
    x = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "c":
                x += 1
    return x


field_size = int(input())
commands = deque(input().split())
field = [input().split() for _ in range(field_size)]
while commands:
    direction = commands.popleft()
    row, col = find_miner(field)
    field[row][col] = "*"
    if direction == "up" and row-1 in range(len(field)):
        row -= 1
    elif direction == "down" and row+1 in range(len(field)):
        row += 1
    elif direction == "left" and col-1 in range(len(field[0])):
        col -= 1
    elif direction == "right" and col+1 in range(len(field[0])):
        col += 1
    else:
        field[row][col] = "s"
        continue

    if field[row][col] == "e":
        print(f"Game over! ({row}, {col})")
        exit()

    field[row][col] = "s"
    if not left_coal(field):
        print(f"You collected all coal! ({row}, {col})")
        exit()

row, col = find_miner(field)
remaining_coal = left_coal(field)
print(f"{remaining_coal} pieces of coal left. ({row}, {col})")
