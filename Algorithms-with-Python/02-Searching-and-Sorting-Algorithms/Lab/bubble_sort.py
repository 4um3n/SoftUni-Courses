import time


# def bubble_sort(numbers, max_iter, swap=False):
#     for i in range(1, max_iter):
#         if numbers[i] < numbers[i - 1]:
#             swap = True
#             numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
#
#     if not swap:
#         return numbers
#
#     return bubble_sort(numbers, max_iter - 1)


def bubble_sort(numbers):
    max_iter = len(numbers)
    swap = True

    while swap:
        swap = False

        for i in range(1, max_iter):
            if numbers[i] < numbers[i - 1]:
                swap = True
                numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

        max_iter -= 1

    return numbers


def main():
    nums = [int(n) for n in input().split()]
    s = time.time()
    print(*bubble_sort(nums), sep=' ')
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
