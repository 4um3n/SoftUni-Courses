import re

planets = {"A": [], "D": []}
star_pattern = r"[s, t, a, r]"
planets_pattern = r"@([A-Za-z]+)[^>!@:-]*:(\d+)!([A|D])![^>!@:-]*->(\d+)"
for _ in range(int(input())):
    line = input()
    c = len(re.findall(star_pattern, line, re.IGNORECASE))
    line = ''.join(chr(ord(ch) - c) for ch in line)
    line = re.findall(planets_pattern, line)
    if line:
        planet_name, attack_type = line[0][0], line[0][2]
        if attack_type == "A":
            planets["A"].append(planet_name)
        elif attack_type == "D":
            planets["D"].append(planet_name)

print(f"Attacked planets: {len(planets['A'])}")
for p in sorted(planets['A']):
    print(f"-> {p}")

print(f"Destroyed planets: {len(planets['D'])}")
for p in sorted(planets['D']):
    print(f"-> {p}")
