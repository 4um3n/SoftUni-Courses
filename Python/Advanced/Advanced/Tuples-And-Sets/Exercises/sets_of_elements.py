a, b = input().split()
set1 = set(input() for _ in range(int(a)))
set2 = set(input() for _ in range(int(b)))
print('\n'.join(set1 & set2))
