numbers = [int(num) for num in input().split()]
removing_count = int(input())
removing_items = (numbers.copy())
removing_items.sort()

for i in range(removing_count):
    numbers.remove(removing_items[i])

print(', '.join(str(n) for n in numbers))
