from collections import deque


def set_dp_outer_layers(rows, cols, matrix, dp):
    dp[0][0] = matrix[0][0]

    for r in range(1, rows):
        dp[r][0] = matrix[r][0] + dp[r - 1][0]

    for c in range(1, cols):
        dp[0][c] = matrix[0][c] + dp[0][c - 1]

    return dp


def get_dp(rows, cols, matrix):
    dp = [[0] * cols for _ in range(rows)]
    set_dp_outer_layers(rows, cols, matrix, dp)

    for row in range(1, rows):
        for col in range(1, cols):
            left = dp[row][col - 1]
            up = dp[row - 1][col]

            if left >= up:
                dp[row][col] = matrix[row][col] + left
            else:
                dp[row][col] = matrix[row][col] + up

    return dp


def get_path(row, col, dp):
    path = deque()
    row -= 1
    col -= 1

    while row > 0 and col > 0:
        path.appendleft([row, col])

        left = dp[row][col - 1]
        up = dp[row - 1][col]

        if left >= up:
            col -= 1
        else:
            row -= 1

    while row > 0:
        path.appendleft([row, col])
        row -= 1

    while col > 0:
        path.appendleft([row, col])
        col -= 1

    path.appendleft([row, col])
    return path


def main():
    rows = int(input())
    cols = int(input())
    matrix = [[int(n) for n in input().split()] for _ in range(rows)]
    dp = get_dp(rows, cols, matrix)
    path = get_path(rows, cols, dp)
    result = ' '.join([f'[{cell[0]}, {cell[1]}]' for cell in path])
    return result


if __name__ == '__main__':
    print(main())
