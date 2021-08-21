number = int(input())
is_valid = False

if number == 0 or 100 <= number <= 200:
    is_valid = True

if not is_valid:
    print(f"invalid")
