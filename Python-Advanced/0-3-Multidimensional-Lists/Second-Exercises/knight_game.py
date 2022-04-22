class Chess:
    def __init__(self, field):
        self.field = field
        self.killed_knights = 0

    @staticmethod
    def get_moves(row, col):
        return [
            (row - 2, col - 1),
            (row - 2, col + 1),
            (row + 2, col - 1),
            (row + 2, col + 1),
            (row - 1, col - 2),
            (row - 1, col + 2),
            (row + 1, col - 2),
            (row + 1, col + 2)
        ]

    def get_knights_positions(self):
        knights_positions = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.field[row][col] == "K":
                    knights_positions.append((row, col))

        return knights_positions

    def get_current_knight_kills_count(self, row, col):
        kills_count = 0
        moves = self.get_moves(row, col)
        for row, col in moves:
            if row in range(len(self.field)) and col in range(len(self.field[row])) and self.field[row][col] == "K":
                kills_count += 1

        return kills_count

    def get_knight_with_max_kills(self):
        kills_count = 0
        row, col = None, None
        knights_positions = self.get_knights_positions()
        for r1, c1 in knights_positions:
            current_kills = self.get_current_knight_kills_count(r1, c1)
            if current_kills > kills_count:
                kills_count = current_kills
                row, col = r1, c1

        return row, col

    def kill_knight(self, row, col):
        self.field[row][col] = 0


matrix = [list(input()) for _ in range(int(input()))]
chess = Chess(matrix)
r, c = chess.get_knight_with_max_kills()
while r is not None and c is not None:
    chess.kill_knight(r, c)
    chess.killed_knights += 1
    r, c = chess.get_knight_with_max_kills()

print(chess.killed_knights)
