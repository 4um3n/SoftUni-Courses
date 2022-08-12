def di(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1
    dp = [[0] * cols for _ in range(rows)]

    for row in range(1, rows):
        dp[row][0] = row

    for col in range(1, cols):
        dp[0][col] = col * 2

    for row in range(1, rows):
        for col in range(1, cols):
            if word1[row - 1] == word2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                left = dp[row][col - 1]
                up = dp[row - 1][col]
                dp[row][col] = min(left, up) + 1

    return dp[rows - 1][cols - 1]


def main():
    word1 = input()
    word2 = input()
    return f'Deletions and Insertions: {di(word1, word2)}'


if __name__ == '__main__':
    print(main())
