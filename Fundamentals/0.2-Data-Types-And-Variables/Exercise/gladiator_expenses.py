lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
broken_shields_count = 0

for day in range(1, lost_fights_count + 1):
    is_helmet_broken = False
    is_sword_broken = False

    if day % 2 == 0:
        is_helmet_broken = True
        expenses += helmet_price

    if day % 3 == 0:
        is_sword_broken = True
        expenses += sword_price

    if is_helmet_broken and is_sword_broken:
        expenses += shield_price
        broken_shields_count += 1

    if broken_shields_count % 2 == 0 and broken_shields_count != 0:
        expenses += armor_price
        broken_shields_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
