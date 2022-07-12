import time


# def insertion_sort(numbers, ind=0):
#     if ind >= len(numbers):
#         return numbers
#
#     i = ind
#
#     while i > 0 and numbers[i] < numbers[i - 1]:
#         numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
#         i -= 1
#
#     return insertion_sort(numbers, ind + 1)


def insertion_sort(numbers):
    for ind in range(len(numbers)):
        i = ind

        while i > 0 and numbers[i] < numbers[i - 1]:
            numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
            i -= 1

    return numbers


def main():
    nums = [int(n) for n in input().split()]
    s = time.time()
    print(*insertion_sort(nums), sep=' ')
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
