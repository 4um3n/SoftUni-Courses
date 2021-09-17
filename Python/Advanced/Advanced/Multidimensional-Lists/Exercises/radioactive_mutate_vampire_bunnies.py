from collections import deque


def find_player(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "P":
                return r, c


def find_bunnies(grid):
    bunnies = [(r, c) for r in range(len(grid)) for c in range(len(grid[r])) if grid[r][c] == "B"]
    return bunnies


def spread_bunnies(bunnies, grid):
    for r, c in bunnies:
        if r-1 in range(len(grid)):
            grid[r-1][c] = "B"
        if r+1 in range(len(grid)):
            grid[r+1][c] = "B"
        if c-1 in range(len(grid[0])):
            grid[r][c-1] = "B"
        if c+1 in range(len(grid[0])):
            grid[r][c+1] = "B"

    return grid


rows, cols = [int(n) for n in input().split()]
field = [list(input()) for _ in range(rows)]
commands = deque(input())
while commands:
    direction = commands.popleft()
    row, col = find_player(field)
    field[row][col] = "."
    if direction == "U" and row-1 in range(len(field)):
        row -= 1
    elif direction == "D" and row+1 in range(len(field)):
        row += 1
    elif direction == "L" and col-1 in range(len(field[0])):
        col -= 1
    elif direction == "R" and col+1 in range(len(field[0])):
        col += 1
    else:
        field = spread_bunnies(find_bunnies(field), field)
        [print(''.join(field[r])) for r in range(len(field))]
        print(f"won: {row} {col}")
        exit()

    field = spread_bunnies(find_bunnies(field), field)
    if field[row][col] == "B":
        [print(''.join(field[r])) for r in range(len(field))]
        print(f"dead: {row} {col}")
        exit()
    else:
        field[row][col] = "P"
