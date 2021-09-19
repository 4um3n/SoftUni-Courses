def find_alice(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "A":
                return r, c


def play(field, r, c):
    field[r][c] = "*"
    tea_bags = 0
    move = input()
    while move:
        if move == "up":
            r -= 1
        elif move == "down":
            r += 1
        elif move == "left":
            c -= 1
        elif move == "right":
            c += 1

        if r not in range(len(field)) or c not in range(len(field[r])):
            print(f"Alice didn't make it to the tea party.")
            break

        if field[r][c] == "R":
            field[r][c] = "*"
            print(f"Alice didn't make it to the tea party.")
            break

        try:
            current_tea_bags = int(field[r][c])
        except ValueError:
            current_tea_bags = 0

        tea_bags += current_tea_bags
        field[r][c] = "*"
        if tea_bags >= 10:
            print(f"She did it! She went to the party.")
            break

        move = input()

    return field


matrix = [input().split() for _ in range(int(input()))]
matrix = play(matrix, *find_alice(matrix))
[print(' '.join(matrix[r])) for r in range(len(matrix))]
