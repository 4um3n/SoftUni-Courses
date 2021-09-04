countries = input().split(", ")
capitals = input().split(", ")
countries = {cou: cap for cou, cap in zip(countries, capitals)}
for cou, cap in countries.items():
    print(f"{cou} -> {cap}")