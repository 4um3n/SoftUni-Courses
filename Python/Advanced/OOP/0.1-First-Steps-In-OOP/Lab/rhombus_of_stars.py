def create_rhombus(rows, symbol='*'):
    def draw_line():
        line = ' ' * (rows - r - 1)
        line += ' '.join([f"{symbol}" for _ in range(r + 1)])
        return line

    lines = []
    for r in range(rows):
        lines.append(draw_line())

    for r in range(rows - 2, -1, -1):
        lines.append(draw_line())

    return '\n'.join(lines)


print(create_rhombus(int(input())))
