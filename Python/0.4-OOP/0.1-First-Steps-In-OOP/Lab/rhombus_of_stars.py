def draw_line(rows, symbol, row):
    line = ' ' * (rows - row - 1)
    line += ' '.join([f"{symbol}" for _ in range(row + 1)])
    return line


def create_rhombus(rows, symbol='*'):
    lines = []
    for r in range(rows):
        lines.append(draw_line(rows, symbol, r))

    for r in range(rows - 2, -1, -1):
        lines.append(draw_line(rows, symbol, r))

    return '\n'.join(lines)


print(create_rhombus(int(input())))
