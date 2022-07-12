# 0 1 2 3 4 5
# 1 2 3 4 5 6
# L   M     R
# M = f(L, R) => (L + R) // 2
# f(0, 5) => (0 + 5) // 2 == 2

def binary_search(numbers, target, left_ind, right_ind):
    if left_ind > right_ind:
        return -1

    middle_ind = (left_ind + right_ind) // 2
    middle_elem = numbers[middle_ind]

    if middle_elem < target:
        left_ind = middle_ind + 1
    elif middle_elem > target:
        right_ind = middle_ind - 1
    else:
        return middle_ind

    return binary_search(numbers, target, left_ind, right_ind)


nums = [int(n) for n in input().split()]
targ = int(input())
print(binary_search(nums, targ, 0, len(nums) - 1))
