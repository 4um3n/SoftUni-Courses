number = int(input())

is_zero = False
is_in_range = False

if -100 <= number <= 100:
    is_in_range = True
    if number == 0:
        is_zero = True

if is_zero:
    print("No")
elif is_in_range:
    print(f"Yes")
else:
    print(f"No")
