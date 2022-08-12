def get_binomial_coefficient(row, col, cache: dict):
    if row < 1 or col < 1 or row == col:
        return 1

    key = f'{row} {col}'

    if key not in cache:
        cache[key] = get_binomial_coefficient(row - 1, col - 1, cache) + get_binomial_coefficient(row - 1, col, cache)

    return cache[key]


def main():
    row = int(input())
    col = int(input())
    return get_binomial_coefficient(row, col, {})


if __name__ == '__main__':
    print(main())
