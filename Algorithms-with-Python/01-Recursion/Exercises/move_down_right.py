def get_moves(rows, cols, row=0, col=0):
    def is_inbound():
        return row < rows and col < cols

    def is_end():
        return row == rows - 1 and col == cols - 1

    if is_end():
        return 1

    if not is_inbound():
        return 0

    return get_moves(rows, cols, row + 1, col) + get_moves(rows, cols, row, col + 1)


r = int(input())
c = int(input())
print(get_moves(r, c))
