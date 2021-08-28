numbers = [int(n) for n in input().split(", ")]
for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers.append(numbers.pop(numbers.index(0)))

print(numbers)
