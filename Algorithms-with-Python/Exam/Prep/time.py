from collections import deque


def lcs(row1, row2):
    rows = len(row1) + 1
    cols = len(row2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for row in range(1, rows):
        for col in range(1, cols):
            if row1[row - 1] == row2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                left = dp[row][col - 1]
                up = dp[row - 1][col]
                dp[row][col] = max(left, up)

    return dp


def get_path(dp, row1, row2):
    path = deque()
    row = len(row1)
    col = len(row2)

    while row > 0 and col > 0:
        if row1[row - 1] == row2[col - 1]:
            path.appendleft(row1[row - 1])
            row -= 1
            col -= 1
        elif dp[row][col - 1] >= dp[row - 1][col]:
            col -= 1
        else:
            row -= 1

    return path


def main():
    row1 = [int(n) for n in input().split()]
    row2 = [int(n) for n in input().split()]
    dp = lcs(row1, row2)
    return '\n'.join([
        ' '.join([str(n) for n in get_path(dp, row1, row2)]),
        str(dp[len(row1)][len(row2)])
    ])


if __name__ == '__main__':
    print(main())
