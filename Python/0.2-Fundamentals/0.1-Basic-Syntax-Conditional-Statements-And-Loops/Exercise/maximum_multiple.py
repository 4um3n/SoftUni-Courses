d = int(input())
b = int(input())
biggest = 0

for n in range(d + 1, b + 1):

    if not n % d == 0:
        continue

    if not n <= b:
        continue

    if not n > 0:
        continue

    if biggest < n:
        biggest = n

print(biggest)
