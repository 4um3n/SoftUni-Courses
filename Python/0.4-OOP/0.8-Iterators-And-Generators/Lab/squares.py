def squares(n: int) -> tuple:
    start = 1
    while start <= n:
        yield start * start
        start += 1


print(squares(5))
b = squares(5)
for el in b:
    print(el)

for el in b:
    print(el)

a = 5
