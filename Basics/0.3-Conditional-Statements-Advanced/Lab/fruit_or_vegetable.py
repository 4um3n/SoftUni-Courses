product = input().lower()

fruit = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegetable = ["tomato", "cucumber", "pepper", "carrot"]

if product in fruit:
    print(f"fruit")
elif product in vegetable:
    print(f"vegetable")
else:
    print(f"unknown")
