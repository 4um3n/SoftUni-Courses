a, b = [int(n) for n in input().split()]
set1 = set(input() for _ in range(a))
set2 = set(input() for _ in range(b))
print('\n'.join(set1 & set2))
