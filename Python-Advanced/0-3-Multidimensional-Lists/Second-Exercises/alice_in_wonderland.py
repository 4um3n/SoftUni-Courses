class Alice:
    __directions = {
        "up": lambda r, c: (r-1, c),
        "down": lambda r, c: (r+1, c),
        "left": lambda r, c: (r, c-1),
        "right": lambda r, c: (r, c+1),
    }

    def __init__(self, field):
        self.field = field
        self.tea_bags = 0
        self.row, self.col = self.get_alice_position()

    def get_alice_position(self):
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                if self.field[r][c] == "A":
                    self.field[r][c] = "*"
                    return r, c

    def move(self, direction):
        self.row, self.col = Alice.__directions[direction](self.row, self.col)

    def check_move(self):
        if self.row not in range(len(self.field)) or self.col not in range(len(self.field[self.row])):
            return False
        elif self.field[self.row][self.col] == "R":
            self.field[self.row][self.col] = "*"
            return False

        self.tea_bags += 0 if not self.field[self.row][self.col].isdigit() else int(self.field[self.row][self.col])
        self.field[self.row][self.col] = "*"
        return True


matrix = [input().split() for _ in range(int(input()))]
alice = Alice(matrix)
while alice.tea_bags < 10:
    move = input()
    alice.move(move)
    if not alice.check_move():
        print(f"Alice didn't make it to the tea party.")
        break

else:
    print(f"She did it! She went to the party.")

[print(' '.join(alice.field[r])) for r in range(len(alice.field))]
