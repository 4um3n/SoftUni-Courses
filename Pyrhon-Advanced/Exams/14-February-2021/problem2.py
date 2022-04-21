def find_player(field):
    for r in range(len(field)):
        for c in range(len(field)):
            if field[r][c] == "P":
                return r, c


matrix_size = int(input())
matrix = [input().split() for _ in range(matrix_size)]
possible_moves = {
    "up": lambda r, c: (r-1, c),
    "down": lambda r, c: (r+1, c),
    "left": lambda r, c: (r, c-1),
    "right": lambda r, c: (r, c+1)
}

coins = 0
path = []
row, col = find_player(matrix)

while coins < 100:
    direction = input()
    if direction not in possible_moves:
        continue

    row, col = possible_moves[direction](row, col)

    if row not in range(len(matrix)) or col not in range(len(matrix[row])) or matrix[row][col] == "X":
        coins //= 2
        print(f"Game over! You've collected {coins} coins.")
        break

    coins += int(matrix[row][col])
    path.append([row, col])
else:
    print(f"You won! You've collected {coins} coins.")

print(f"Your path: ")
[print(el) for el in path]
