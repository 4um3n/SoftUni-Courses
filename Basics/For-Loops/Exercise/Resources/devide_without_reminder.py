numbers_count = int(input())
p1 = 0
p2 = 0
p3 = 0

for n in range(numbers_count):
    current_number = int(input())

    if current_number % 2 == 0:
        p1 += 1

    if current_number % 3 == 0:
        p2 += 1

    if current_number % 4 == 0:
        p3 += 1

p1 = p1 / numbers_count * 100
p2 = p2 / numbers_count * 100
p3 = p3 / numbers_count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
