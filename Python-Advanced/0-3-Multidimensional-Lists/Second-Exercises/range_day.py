class Shooter:
    __directions = {
        "up": lambda r, c: (r-1, c),
        "down": lambda r, c: (r+1, c),
        "left": lambda r, c: (r, c-1),
        "right": lambda r, c: (r, c+1),
    }

    def __init__(self, field):
        self.field = field
        self.shoot_targets = []
        self.total_targets_count = sum([field[r].count("x") for r in range(len(field))])

    def find_shooter(self):
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                if self.field[r][c] == "A":
                    return r, c

    def move(self, direction, steps):
        r, c = self.find_shooter()
        r1, c1 = r, c
        for _ in range(steps):
            r1, c1 = Shooter.__directions[direction](r1, c1)

        if r1 in range(len(self.field)) and c1 in range(len(self.field[r1])) and self.field[r1][c1] == ".":
            self.field[r][c] = "."
            self.field[r1][c1] = "A"
            return

    def shoot(self, direction):
        r, c = self.find_shooter()
        while self.field[r][c] != "x":
            r, c = Shooter.__directions[direction](r, c)

            if r not in range(len(self.field)) or c not in range(len(self.field[r])):
                return self.shoot_targets

        self.shoot_targets.append([r, c])
        self.field[r][c] = "."
        return self.shoot_targets


matrix = [input().split() for _ in range(5)]
shooter = Shooter(matrix)

for _ in range(int(input())):
    command = input().split()

    if "move" in command:
        direct, steps_count = command[1], int(command[2])
        shooter.move(direct, steps_count)

    elif "shoot" in command:
        direct = command[1]
        shooter.shoot(direct)

    if len(shooter.shoot_targets) == shooter.total_targets_count:
        print(f"Training completed! All {shooter.total_targets_count} targets hit.")
        break
else:
    print(f"Training not completed! {shooter.total_targets_count - len(shooter.shoot_targets)} targets left.")

[print(shooter.shoot_targets[r]) for r in range(len(shooter.shoot_targets))]
