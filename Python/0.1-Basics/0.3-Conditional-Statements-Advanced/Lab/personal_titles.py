age = float(input())
gender = input().lower()

if gender == "m":
    if age < 16:
        print(f"Master")
    else:
        print(f"Mr.")
else:
    if age < 16:
        print(f"Miss")
    else:
        print(f"Ms.")
