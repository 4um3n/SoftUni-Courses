import sys

numbers_count = int(input())
total_sum = 0
biggest_number = -sys.maxsize

for i in range(numbers_count):
    current_number = int(input())
    total_sum += current_number

    if current_number > biggest_number:
        biggest_number = current_number

total_sum -= biggest_number

if biggest_number == total_sum:
    print(f"Yes\n"
          f"Sum = {total_sum}")
else:
    print(f"No\n"
          f"Diff = {abs(total_sum - biggest_number)}")
