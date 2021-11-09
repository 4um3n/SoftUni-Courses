def read_next(*sequences):
    for sequence in sequences:
        for el in sequence:
            yield el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
