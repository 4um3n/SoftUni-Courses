cars = set()
for _ in range(int(input())):
    command, number_plate = input().split(", ")
    if command == "IN":
        cars.add(number_plate)
    elif command == "OUT" and number_plate in cars:
        cars.remove(number_plate)

if cars:
    print('\n'.join(cars))
else:
    print(f"Parking Lot is Empty")
