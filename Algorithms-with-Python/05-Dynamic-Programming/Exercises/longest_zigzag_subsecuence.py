from collections import deque


def lzs(numbers):
    parents = [[None] * len(numbers) for _ in range(2)]
    dp = [[0] * len(numbers) for _ in range(2)]
    dp[0][0] = dp[1][0] = 1
    best_row, best_col, best_size = 0, 0, 0

    for idx in range(1, len(numbers)):
        current_number = numbers[idx]

        for prev_idx in range(idx - 1, -1, -1):
            prev_number = numbers[prev_idx]
            size, row = 0, 0

            if current_number > prev_number and dp[1][prev_idx] + 1 >= dp[0][idx]:
                row = 0
                size = dp[1][prev_idx] + 1
                dp[row][idx] = size
                parents[row][idx] = prev_idx
            elif current_number < prev_number and dp[0][prev_idx] + 1 >= dp[1][idx]:
                row = 1
                size = dp[0][prev_idx] + 1
                dp[row][idx] = size
                parents[row][idx] = prev_idx

            if size > best_size:
                best_size = size
                best_row = row
                best_col = idx

    return parents, best_row, best_col


def get_path(numbers, parents, row, col):
    sequence = deque()

    while col is not None:
        sequence.appendleft(numbers[col])
        col = parents[row][col]
        row = 1 if row == 0 else 0

    return sequence


def main():
    numbers = [int(n) for n in input().split()]
    parents, best_row, best_col = lzs(numbers)
    return ' '.join([str(n) for n in get_path(numbers, parents, best_row, best_col)])


if __name__ == '__main__':
    print(main())
