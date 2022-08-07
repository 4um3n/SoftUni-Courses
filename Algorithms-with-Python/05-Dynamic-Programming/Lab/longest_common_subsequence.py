from collections import deque


def lcs(first, second):
    rows = len(first) + 1
    cols = len(second) + 1
    dp = [[0] * cols for _ in range(rows)]

    for r in range(1, rows):
        for c in range(1, cols):
            if first[r - 1] == second[c - 1]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                left = dp[r][c - 1]
                up = dp[r - 1][c]
                dp[r][c] = max(left, up)

    return dp


def get_path(first, second, dp):
    row = len(dp) - 1
    col = len(dp[0]) - 1
    path = deque()

    while row > 0 and col > 0:
        up = dp[row - 1][col]
        left = dp[row][col - 1]

        if first[row - 1] == second[col - 1]:
            path.appendleft(first[row - 1])
            row -= 1
            col -= 1
        elif up > left:
            row -= 1
        else:
            col -= 1

    return path


def main():
    first = input()
    second = input()
    dp = lcs(first, second)
    # path = get_path(first, second, dp)
    # print(''.join(path))
    return dp[len(dp) - 1][len(dp[0]) - 1]


if __name__ == '__main__':
    print(main())
