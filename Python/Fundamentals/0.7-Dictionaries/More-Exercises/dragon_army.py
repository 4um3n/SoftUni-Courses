dragons = {}
for _ in range(int(input())):
    d_type, d_name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    
    damage, health, armor = int(damage), int(health), int(armor)
    if d_type not in dragons:
        dragons[d_type] = {}
    
    dragons[d_type].update({d_name: {"d": damage, "h": health, "a": armor}})

for d_type, values in dragons.items():
    group_d = [v["d"] for v in values.values()]
    group_h = [v["h"] for v in values.values()]
    group_a = [v["a"] for v in values.values()]
    average_d = sum(group_d) / len(group_d)
    average_h = sum(group_h) / len(group_h)
    average_a = sum(group_a) / len(group_a)
    print(f"{d_type}::({average_d:.2f}/{average_h:.2f}/{average_a:.2f})")
    for n, v in sorted(values.items()):
        print(f"-{n} -> damage: {v['d']}, health: {v['h']}, armor: {v['a']}")
