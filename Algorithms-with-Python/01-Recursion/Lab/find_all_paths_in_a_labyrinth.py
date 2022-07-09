def find_paths(field, row=0, col=0, direction='', path=[], result=[]):
    def is_inbound():
        return 0 <= row < len(field) and 0 <= col < len(field[row])

    def is_free():
        return field[row][col] == '-'

    def is_exit():
        return field[row][col].lower() == 'e'

    def mark():
        field[row][col] = 'v'

    def unmark():
        field[row][col] = '-'

    if not is_inbound():
        return

    path.append(direction)

    if is_exit():
        result.append(''.join(path))
    elif is_free():
        mark()
        find_paths(field, row, col + 1, 'R', path, result)
        find_paths(field, row, col - 1, 'L', path, result)
        find_paths(field, row - 1, col, 'U', path, result)
        find_paths(field, row + 1, col, 'D', path, result)
        unmark()

    path.pop()
    return '\n'.join(result)


r = int(input())
c = int(input())
labyrinth = [list(input()) for _ in range(r)]
print(find_paths(labyrinth))
