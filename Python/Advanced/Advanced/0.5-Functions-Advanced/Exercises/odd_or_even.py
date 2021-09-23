def odd_or_even_sum(command, nums, nums_len, result=None):
    if command == "Odd" and result is None:
        nums = list(filter(lambda x: x % 2 == 1, nums))
        result = 0
    elif command == "Even" and result is None:
        nums = list(filter(lambda x: x % 2 == 0, nums))
        result = 0

    if not nums:
        return result * nums_len

    result += nums.pop(0)
    return odd_or_even_sum(command, nums, nums_len, result)


command_data = input()
nums_data = list(map(int, input().split()))
print(odd_or_even_sum(command_data, nums_data, len(nums_data)))
