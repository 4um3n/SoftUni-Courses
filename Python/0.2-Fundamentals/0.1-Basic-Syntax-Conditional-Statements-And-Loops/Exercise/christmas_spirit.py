quantity = int(input())
days_count = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
total_cost = 0
spirit_points = 0

for day in range(1, days_count + 1):
    garlands = False
    lights = False

    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += ornament_set_price * quantity
        spirit_points += 5

    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garlands_price) * quantity
        spirit_points += 13
        garlands = True

    if day % 5 == 0:
        total_cost += tree_lights_price * quantity
        spirit_points += 17
        lights = True

    if day % 10 == 0:
        spirit_points -= 20
        total_cost += tree_lights_price + tree_garlands_price + tree_skirt_price

    if garlands and lights:
        spirit_points += 30

if days_count % 10 == 0:
    spirit_points -= 30

print(f"Total cost: {total_cost}\n"
      f"Total spirit: {spirit_points}")
