budget = float(input())
a_kg_of_flour_price = float(input())
a_litre_of_milk_price = a_kg_of_flour_price + a_kg_of_flour_price * 0.25
a_pack_of_eggs_price = a_kg_of_flour_price * 0.75
a_quarter_of_milk_price = a_litre_of_milk_price / 4
cozonac_price = a_pack_of_eggs_price + a_kg_of_flour_price + a_quarter_of_milk_price
cozonacs_made = 0
colored_eggs = 0

while budget > 0:
    if cozonac_price > budget:
        break

    budget -= cozonac_price
    cozonacs_made += 1
    colored_eggs += 3

    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2

print(f"You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
