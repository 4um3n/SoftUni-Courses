n = int(input())

for num in range(1111, 10000):
    is_num_special = False

    for digit in str(num):
        digit = int(digit)

        if digit == 0:
            is_num_special = False
            break

        if n % digit == 0:
            is_num_special = True
        else:
            is_num_special = False
            break

    if is_num_special:
        print(num, end=" ")
