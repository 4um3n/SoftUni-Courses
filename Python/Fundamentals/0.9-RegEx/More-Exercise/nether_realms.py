import re

demons = {}
data = input().split(",")
health_pattern = r"[^\d/\+\*\.-]"
damage_pattern = r"([+|-]*\d+(\.\d+)*)"
for name in data:
    name = name.strip()
    health = sum(ord(ch) for ch in re.findall(health_pattern, name)) 
    damage = sum(float(n.group()) for n in re.finditer(damage_pattern, name))
    for sign in re.findall(r"[\*|/]", name):
        if sign == "*":
            damage *= 2
        elif sign == "/":
            damage *= 0.5
    
    demons[name] = {"health": health, "damage": damage}

for n, v in sorted(demons.items()):
    print(f"{n} - {v['health']} health, {v['damage']:.2f} damage")
