def fibonacci(n, mem):
    if n in mem:
        return mem[n]

    if n <= 1:
        return n

    result = fibonacci(n - 1, mem) + fibonacci(n - 2, mem)
    mem[n] = result
    return result


def main():
    n = int(input())
    print(fibonacci(n, {}))


if __name__ == '__main__':
    main()

