def nested_loops(vector, ind=0, result=[]):
    if ind >= len(vector):
        result.append(' '.join(map(lambda num: str(num), vector)))
        return

    for digit in range(1, len(vector) + 1):
        vector[ind] = digit
        nested_loops(vector, ind+1, result)

    return '\n'.join(result)


iterations = int(input())
print(nested_loops([0] * iterations))
