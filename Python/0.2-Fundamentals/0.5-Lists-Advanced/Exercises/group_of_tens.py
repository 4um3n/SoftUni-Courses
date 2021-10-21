from math import ceil

numbers = [int(n) for n in input().split(", ")]
max_groups_count = ceil(max(numbers) / 10)
for i in range(1, max_groups_count + 1):
    print(f"Group of {i}0's: {[n for n in numbers if i * 10 - 10 < n <= i * 10]}")
