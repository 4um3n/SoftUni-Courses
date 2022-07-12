import time


# def selection_sort(numbers, ind=0):
#     if ind >= len(numbers):
#         return numbers
#
#     min_ind = ind
#
#     for i in range(ind + 1, len(numbers)):
#         if numbers[i] < numbers[min_ind]:
#             min_ind = i
#
#     numbers[ind], numbers[min_ind] = numbers[min_ind], numbers[ind]
#     return selection_sort(numbers, ind+1)


def selection_sort(numbers):
    for ind in range(len(numbers)):
        min_ind = ind

        for i in range(ind + 1, len(numbers)):
            if numbers[i] < numbers[min_ind]:
                min_ind = i

        numbers[ind], numbers[min_ind] = numbers[min_ind], numbers[ind]

    return numbers


def main():
    nums = [int(n) for n in input().split()]
    s = time.time()
    print(*selection_sort(nums), sep=' ')
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
