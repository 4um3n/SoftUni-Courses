def reverse_array(array: list, i=0):
    if i == len(array) // 2:
        return

    last_i = len(array) - 1 - i
    array[i], array[last_i] = array[last_i], array[i]
    reverse_array(array, i + 1)


arr = input().split()
reverse_array(arr)
print(' '.join(arr))
