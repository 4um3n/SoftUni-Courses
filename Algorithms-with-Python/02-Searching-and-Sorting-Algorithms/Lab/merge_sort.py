import time


def merge_arrays(left_array, right_array):
    result = [None] * (len(left_array) + len(right_array))
    left_ind = 0
    right_ind = 0
    result_ind = 0

    while left_ind < len(left_array) and right_ind < len(right_array):
        if left_array[left_ind] < right_array[right_ind]:
            result[result_ind] = left_array[left_ind]
            left_ind += 1
        else:
            result[result_ind] = right_array[right_ind]
            right_ind += 1

        result_ind += 1

    while left_ind < len(left_array):
        result[result_ind] = left_array[left_ind]
        left_ind += 1
        result_ind += 1

    while right_ind < len(right_array):
        result[result_ind] = right_array[right_ind]
        right_ind += 1
        result_ind += 1

    return result


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    middle = len(numbers) // 2
    left = numbers[:middle]
    right = numbers[middle:]
    return merge_arrays(merge_sort(left), merge_sort(right))


def main():
    nums = [int(n) for n in input().split()]
    s = time.time()
    print(*merge_sort(nums), sep=' ')
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
