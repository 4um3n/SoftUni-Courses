def recursive_array_sum(array, i=0):
    if i == len(array):
        return 0

    return array[i] + recursive_array_sum(array, i+1)


nums = [int(n) for n in input().split()]
print(recursive_array_sum(nums))
