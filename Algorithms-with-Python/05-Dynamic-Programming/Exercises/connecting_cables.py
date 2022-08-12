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

    return dp[rows - 1][cols - 1]


def main():
    row1 = [int(n) for n in input().split()]
    row2 = [n for n in range(1, len(row1) + 1)]
    return f'Maximum pairs connected: {lcs(row1, row2)}'


if __name__ == '__main__':
    print(main())
