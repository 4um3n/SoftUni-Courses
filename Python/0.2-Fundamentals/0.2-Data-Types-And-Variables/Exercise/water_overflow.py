tank_capacity = 255
current_tank_volume = 0
iterations_count = int(input())

for iteration in range(iterations_count):
    current_water_quantities = int(input())
    if current_tank_volume + current_water_quantities > tank_capacity:
        print(f"Insufficient capacity!")
        continue

    current_tank_volume += current_water_quantities

print(f"{current_tank_volume}")
