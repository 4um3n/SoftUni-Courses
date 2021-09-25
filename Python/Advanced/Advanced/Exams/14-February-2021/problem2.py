def find_player(maze):
    for r in range(len(maze)):
        for c in range(len(maze[r])):
            if maze[r][c] == "P":
                return r, c


def play(maze, r, c, path=[], coins=0):
    if coins >= 100:
        return f"You won! You've collected {coins} coins.", path

    direction = input()
    if direction == "up":
        r -= 1
    elif direction == "down":
        r += 1
    elif direction == "left":
        c -= 1
    elif direction == "right":
        c += 1
    else:
        return play(maze, r, c, path, coins)

    if r not in range(len(maze)) or c not in range(len(maze[r])) or maze[r][c] == "X":
        coins //= 2
        return f"Game over! You've collected {coins} coins.", path

    coins += int(maze[r][c])
    path.append([r, c])
    return play(maze, r, c, path, coins)


matrix = [input().split() for _ in range(int(input()))]
initial_r_c = find_player(matrix)
result, path_data = play(matrix, *initial_r_c)
print(f"{result}\nYour path:")
[print(x) for x in path_data]
