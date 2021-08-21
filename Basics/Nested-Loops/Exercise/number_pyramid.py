num = int(input())
counter = 1
is_break = False

for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(counter, end=" ")
        counter += 1

        if counter > num:
            is_break = True
            break

    if is_break:
        break
    print()
