def create_sequence(n):
    if n < 1:
        return f"Enter number bigger than 0!"

    nums = [0] if n == 1 else [0, 1]
    for i in range(2, n):
        next_n = nums[i-2] + nums[i-1]
        nums.append(next_n)

    return ' '.join([str(n) for n in nums])


def locate_number(nums, n):
    nums, n = nums.split(), str(n)
    try:
        i = nums.index(n)
        return f"The number - {n} is at index {i}"
    except ValueError:
        return f"The number {n} is not in the sequence"
