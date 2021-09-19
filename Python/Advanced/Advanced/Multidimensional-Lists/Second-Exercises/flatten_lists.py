matrix = [data.split() for data in input().split("|")]
print(' '.join([' '.join(el) for el in matrix[::-1] if el]))
