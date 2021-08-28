values = [int(n) for n in input().split()]
print([abs(n) if n <= 0 else -n for n in values])
