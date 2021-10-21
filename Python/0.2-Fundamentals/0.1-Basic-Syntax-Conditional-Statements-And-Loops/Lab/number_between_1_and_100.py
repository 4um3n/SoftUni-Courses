number = float(input())
in_range = range(1, 101)

while True:
    if number in in_range:
        print(f"The number {number:.2f} is between 1 and 100")
        break
