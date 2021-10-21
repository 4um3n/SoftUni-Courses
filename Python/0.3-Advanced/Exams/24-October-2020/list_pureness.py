def best_list_pureness(nums, n, current_n=0, cycles=0, pureness=None):
    if cycles == n+1:
        return f"Best pureness {pureness} after {current_n} rotations"

    current_pureness = sum([nums[i] * i for i in range(len(nums))])
    if pureness is None or current_pureness > pureness:
        pureness = current_pureness
        current_n = cycles

    cycles += 1
    nums.insert(0, nums.pop())
    return best_list_pureness(nums, n, current_n, cycles, pureness)
