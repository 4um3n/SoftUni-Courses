interval_start = int(input())
interval_end = int(input())
magick_number = int(input())
combinations_counter = 0
is_combination_found = False

for x in range(interval_start, interval_end + 1):
    for y in range(interval_start, interval_end + 1):
        combination = x + y
        combinations_counter += 1

        if combination == magick_number:
            is_combination_found = True
            break

    if is_combination_found:
        break

if is_combination_found:
    print(f"Combination N:{combinations_counter} ({x} + {y} = {magick_number})")
else:
    print(f"{combinations_counter} combinations - neither equals {magick_number}")
