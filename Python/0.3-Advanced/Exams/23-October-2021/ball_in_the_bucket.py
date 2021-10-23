class Shooter:
    def __init__(self, field):
        self.field = field
        self.total_score = 0

    def check_shoot(self, row, col):
        if row in range(len(self.field)) and col in range(len(self.field[row])) and self.field[row][col] == "B":
            self.field[row][col] = '0'
            return True
        return False

    def get_score(self, col):
        for row in range(len(self.field)):
            if self.field[row][col].isdigit():
                self.total_score += int(self.field[row][col])


matrix = [input().split() for _ in range(6)]
shooter = Shooter(matrix)
prizes = {
    "Football": range(100, 200),
    "Teddy Bear": range(200, 300),
    "Lego Construction Set": 300,
}

for _ in range(3):
    r, c = [int(n) for n in input()[1:-1].split(', ')]
    if shooter.check_shoot(r, c):
        shooter.get_score(c)

for k, v in prizes.items():
    if k != "Lego Construction Set" and shooter.total_score in v or k == "Lego Construction Set" and shooter.total_score >= v:
        print(f"Good job! You scored {shooter.total_score} points, and you've won {k}.")
        break
else:
    print(f"Sorry! You need {100 - shooter.total_score} points more to win a prize.")
