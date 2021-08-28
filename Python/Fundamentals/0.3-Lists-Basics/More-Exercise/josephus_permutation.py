numbers = [int(n) for n in input().split()]
index, new_numbers, counter = -1, [], int(input())
while len(numbers) > 0:
    for _ in range(counter):
        index += 1
        if index == len(numbers):
            index = 0

    new_numbers.append(numbers.pop(index))
    index -= 1

new_numbers = repr(new_numbers).replace(" ", "")
print(new_numbers)
