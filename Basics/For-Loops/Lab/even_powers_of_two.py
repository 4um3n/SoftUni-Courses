n = int(input())

for i in range(2**n + 1):
    if i % 2 == 0:
        print(2**i)
    if 2**i >= 2**n:
        break
