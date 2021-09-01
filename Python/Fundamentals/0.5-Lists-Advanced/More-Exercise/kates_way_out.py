def find_kate():
    for r in range(len(initial_maze)):
        for c in range(len(initial_maze[r])):
            if initial_maze[r][c] == "k":
                return [r, c]


def check_chain(x, y):
    if maze[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        return check_chain(x - 1, y) + check_chain(x + 1, y) + check_chain(x, y - 1) + check_chain(x, y + 1)
    return 1 if maze[x][y] == 2 else 0


def moves_count(x, y):
    if maze[x][y] == 1 and not visited[x][y]:
        visited[x][y] = True
        return moves_count(x - 1, y) + moves_count(x + 1, y) + moves_count(x, y - 1) + moves_count(x, y + 1) + 1
    return 0


initial_maze = [list(f"#{input()}#") for _ in range(int(input()))]
maze = [[1 if initial_maze[r][c] == " " else 0 for c in range(len(initial_maze[0]))] for r in range(len(initial_maze))]
maze.append([2 for _ in range(len(initial_maze[0]))])
maze.insert(0, [2 for _ in range(len(initial_maze[0]))])
for i in range(len(maze)):
    maze[i][0] = 2
    maze[i][-1] = 2

visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
x1, y1 = find_kate()
maze[x1 + 1][y1] = 1
is_out = check_chain(x1 + 1, y1)
if not is_out:
    print(f"Kate cannot get out")
else:
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    moves = moves_count(x1 + 1, y1)
    print(f"Kate got out in {moves} moves")
