def generate_vectors(vector: list, ind=0, digits=2, result=[]):
    if ind >= len(vector):
        result.append(''.join(map(lambda n: str(n), vector)))
        return

    for digit in range(digits):
        vector[ind] = digit
        generate_vectors(vector, ind + 1, digits, result)

    return '\n'.join(result)


vector_length = int(input())
print(generate_vectors([0] * vector_length))
