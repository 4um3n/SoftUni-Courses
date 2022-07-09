def get_queens_disposal(board, row=0, cols=[], left=[], right=[], result=[]):
    def can_place(r, c):
        return board[r][c] == '-' and c not in cols and c - r not in left and c + r not in right

    def place_queen(r, c):
        board[r][c] = '*'
        cols.append(c)
        left.append(c - r)
        right.append(c + r)

    def remove_queen(r, c):
        board[r][c] = '-'
        cols.remove(c)
        left.remove(c - r)
        right.remove(c + r)

    if row == len(board):
        result.append('\n'.join([' '.join(r) for r in board]))
        return

    for col in range(8):
        if can_place(row, col):
            place_queen(row, col)
            get_queens_disposal(board, row + 1, cols, left, right, result)
            remove_queen(row, col)

    return '\n\n'.join(result)


chessboard = [['-'] * 8 for _ in range(8)]
print(get_queens_disposal(chessboard))
