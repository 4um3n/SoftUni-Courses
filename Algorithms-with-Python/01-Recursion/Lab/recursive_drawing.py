def draw_figure(rows, result=[]):
    if rows < 1:
        return

    result.append('*' * rows)
    draw_figure(rows - 1, result)
    result.append('#' * rows)
    return '\n'.join(result)


r = int(input())
print(draw_figure(r))
