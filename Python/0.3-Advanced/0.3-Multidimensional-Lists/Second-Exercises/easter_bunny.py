class Bunnie:
    __possible_directions = {
            "up": lambda row, col: (row - 1, col),
            "down": lambda row, col: (row + 1, col),
            "left": lambda row, col: (row, col - 1),
            "right": lambda row, col: (row, col + 1),
        }

    def __init__(self, field):
        self.field = field

    def find_bunny(self):
        for r in range(len(self.field)):
            for c in range(len(self.field[r])):
                if self.field[r][c] == "B":
                    return r, c

    def collect_eggs(self, direction, r, c):
        moves = []
        r, c = Bunnie.__possible_directions[direction](r, c)
        while r in range(len(self.field)) and c in range(len(self.field[r])) and self.field[r][c] != "X":
            moves.append([r, c])
            r, c = Bunnie.__possible_directions[direction](r, c)

        return moves

    def get_collected_eggs_count(self, moves):
        return sum([int(self.field[r][c]) for r, c in moves])


def play(bunnie, directions):
    max_collected_eggs, direction_to_go, made_moves = 0, "", []
    for direction in directions:
        moves = bunnie.collect_eggs(direction, *bunnie.find_bunny())
        collected_eggs = bunnie.get_collected_eggs_count(moves)

        if collected_eggs >= max_collected_eggs:
            max_collected_eggs = collected_eggs
            direction_to_go = direction
            made_moves = moves.copy()

        moves.clear()

    res = f"{direction_to_go}\n"
    res += '\n'.join([f"{made_moves[r]}" for r in range(len(made_moves))])
    res += f"\n{max_collected_eggs}"
    return res


matrix = [input().split() for _ in range(int(input()))]
possible_moves = ["up", "down", "left", "right"]
print(play(Bunnie(matrix), possible_moves))
