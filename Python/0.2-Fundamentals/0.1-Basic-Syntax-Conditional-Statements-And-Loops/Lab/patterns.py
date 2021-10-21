num = int(input())

for row in range(1, num + 1):
    for col in range(1, row + 1):
        print(f"*", end="")

    print()

for row2 in range(num - 1, 0, -1):
    for col2 in range(row2, 0, -1):
        print(f"*", end="")

    print()
