from itertools import permutations


def possible_permutations(numbers: list):
    permutations_data = permutations(numbers, len(numbers))
    for el in permutations_data:
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]
