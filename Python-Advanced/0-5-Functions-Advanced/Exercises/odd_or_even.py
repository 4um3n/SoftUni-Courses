def odd_or_even_sum_multiplied_by_len(odd_or_even, nums, nums_len, result=None):
    if result is None:
        result = 0
        nums = tuple(filter(lambda x: x % 2 == 1 if odd_or_even == "Odd" else x % 2 == 0, nums))

    if not nums:
        return result * nums_len

    return odd_or_even_sum_multiplied_by_len(odd_or_even, nums[1:], nums_len, result+nums[0])


command = input()
numbers_data = tuple(map(int, input().split()))
print(odd_or_even_sum_multiplied_by_len(command, numbers_data, len(numbers_data)))
