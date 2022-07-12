import time


def quick_sort(numbers, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if numbers[left] > numbers[pivot] > numbers[right]:
            numbers[left], numbers[right] = numbers[right], numbers[left]

        if numbers[left] <= numbers[pivot]:
            left += 1

        if numbers[right] >= numbers[pivot]:
            right -= 1

    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
    quick_sort(numbers, pivot, right - 1)
    quick_sort(numbers, left, end)
    return numbers


def main():
    nums = [int(n) for n in input().split()]
    s = time.time()
    print(*quick_sort(nums, 0, len(nums) - 1), sep=' ')
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
