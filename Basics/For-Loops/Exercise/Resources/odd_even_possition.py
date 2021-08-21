import sys

numbers_count = int(input())
odd_sum = 0
even_sum = 0
max_odd_num = -sys.maxsize
min_odd_num = sys.maxsize
max_even_num = -sys.maxsize
min_even_num = sys.maxsize

for index, num in enumerate(range(1, numbers_count + 1)):
    current_number = float(input())

    if not index % 2 == 0:
        even_sum += current_number

        if max_even_num < current_number:
            max_even_num = current_number

        if min_even_num > current_number:
            min_even_num = current_number
    else:
        odd_sum += current_number

        if max_odd_num < current_number:
            max_odd_num = current_number

        if min_odd_num > current_number:
            min_odd_num = current_number

print(f"OddSum={odd_sum:.2f},")
if sys.maxsize == min_odd_num:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd_num:.2f},")

if -sys.maxsize == max_odd_num:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd_num:.2f},")

print(f"EvenSum={even_sum:.2f},")
if sys.maxsize == min_even_num:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even_num:.2f},")

if -sys.maxsize == max_even_num:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_even_num:.2f}")
