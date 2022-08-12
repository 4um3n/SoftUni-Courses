def med(row1, row2, replace, insert, delete):
    rows = len(row1) + 1
    cols = len(row2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for col in range(1, cols):
        dp[0][col] = dp[0][col - 1] + insert

    for row in range(1, rows):
        dp[row][0] = dp[row - 1][0] + delete

    for row in range(1, rows):
        for col in range(1, cols):
            left = dp[row][col - 1]
            up = dp[row - 1][col]
            up_left = dp[row - 1][col - 1]

            if row1[row - 1] == row2[col - 1]:
                dp[row][col] = up_left
            else:
                dp[row][col] = min(left + insert, up + delete, up_left + replace)

    return dp[rows - 1][cols - 1]


def main():
    replace = int(input())
    insert = int(input())
    delete = int(input())
    row1 = input()
    row2 = input()
    return f'Minimum edit distance: {med(row1, row2, replace, insert, delete)}'


if __name__ == '__main__':
    print(main())
    