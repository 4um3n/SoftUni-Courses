def get_area(letter, matrix, row, col, rows, cols, visited):
    if row >= rows or row < 0 or col >= cols or col < 0:
        return 0

    if (row, col) in visited:
        return 0

    if matrix[row][col] != letter:
        return 0

    visited.add((row, col))
    get_area(letter, matrix, row + 1, col, rows, cols, visited)
    get_area(letter, matrix, row - 1, col, rows, cols, visited)
    get_area(letter, matrix, row, col + 1, rows, cols, visited)
    get_area(letter, matrix, row, col - 1, rows, cols, visited)
    return 1


def get_letters(matrix, rows, cols):
    letters = {}
    visited = set()

    for row in range(rows):
        for col in range(cols):
            letter = matrix[row][col]

            if letter not in letters:
                letters[letter] = 0

            letters[letter] += get_area(letter, matrix, row, col, rows, cols, visited)

    return letters


def main():
    rows = int(input())
    cols = int(input())
    matrix = [list(input()) for _ in range(rows)]
    letters = get_letters(matrix, rows, cols)
    message = [f'Areas: {sum(letters.values())}']

    for letter, count in sorted(letters.items(), key=lambda kvp: kvp[0]):
        message.append(f"Letter '{letter}' -> {count}")

    return '\n'.join(message)


if __name__ == '__main__':
    print(main())
