materials = {"shards":  0, "fragments": 0, "motes": 0}
mapper = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}
obtained_legendary_item = None
current_materials = input()
while current_materials:
    current_materials = current_materials.split()
    for i in range(0, len(current_materials), 2):
        quantity, material = int(current_materials[i]), current_materials[i + 1].lower()
        if material not in materials:
            materials[material] = 0
        
        materials[material] += quantity
        if material in mapper and materials[material] >= 250:
            materials[material] -= 250
            obtained_legendary_item = mapper[material]
            print(f"{obtained_legendary_item} obtained!")
            break
    
    if obtained_legendary_item is not None:
        break

    current_materials = input()

junk = {m: q for m, q in materials.items() if m not in mapper}
for m, q in sorted(materials.items(), key=lambda x: (-x[1], x[0])):
    if m in mapper:
        print(f"{m}: {q}")

for m, q in sorted(junk.items()):
    print(f"{m}: {q}")
