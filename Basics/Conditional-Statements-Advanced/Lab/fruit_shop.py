fruit = input().lower()
day = input()
quantity = float(input())
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
price = 0
is_fruit_valid = False
is_day_valid = False
if fruit in fruits:
    is_fruit_valid = True
if day in week:
    is_day_valid = True

    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
elif day in weekend:
    is_day_valid = True

    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

if is_fruit_valid and is_day_valid:
    end_sum = quantity * price
    print(f"{end_sum:.2f}")
else:
    print(f"error")
