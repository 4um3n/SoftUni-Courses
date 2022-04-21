class Christmas:
    __possible_moves = {
        "up": lambda row, col: (row - 1, col),
        "down": lambda row, col: (row + 1, col),
        "left": lambda row, col: (row, col - 1),
        "right": lambda row, col: (row, col + 1),
    }

    def __init__(self, field, presents_count):
        self.field = field
        self.presents_count = presents_count
        self.nice_kids_count = sum([field[r].count("V") for r in range(len(field))])
        self._initial_nice_kids_count = self.nice_kids_count

    def find_santa(self):
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                if self.field[r][c] == "S":
                    return r, c

    def get_next_move(self, direction):
        r, c = self.find_santa()
        r1, c1 = Christmas.__possible_moves[direction](r, c)
        if r1 in range(len(self.field)) and c1 in range(len(self.field[r1])):
            self.field[r][c] = "-"
            return r1, c1
        return r, c

    def check_house(self, r, c):
        if self.field[r][c] == "V":
            self.nice_kids_count -= 1
            self.presents_count -= 1
            self.field[r][c] = "-"

        elif self.field[r][c] == "X":
            self.field[r][c] = "-"

        elif self.field[r][c] == "C":
            self.cookie_rush(r, c)

        self.field[r][c] = "S"

    def cookie_rush(self, r, c):
        kids = ["V", "X"]
        for r, c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if self.field[r][c] in kids and self.presents_count:
                if self.field[r][c] == "V":
                    self.nice_kids_count -= 1

                self.field[r][c] = "-"
                self.presents_count -= 1

    def get_field(self):
        return '\n'.join([f"{' '.join(self.field[r])} " for r in range(len(self.field))])

    def __str__(self):
        if not self.nice_kids_count:
            return f"Good job, Santa! {self._initial_nice_kids_count} happy nice kid/s."
        else:
            return f"No presents for {self.nice_kids_count} nice kid/s."


def change_field(christmas: Christmas):
    direction = input()
    while direction != "Christmas morning":
        christmas.check_house(*christmas.get_next_move(direction))
        if not christmas.presents_count:
            if christmas.nice_kids_count:
                print(f"Santa ran out of presents!")
            break

        direction = input()

    res = christmas.get_field()
    return res


presents = int(input())
matrix = [input().split() for _ in range(int(input()))]
christmas_object = Christmas(matrix, presents)
print(change_field(christmas_object))
print(christmas_object)
