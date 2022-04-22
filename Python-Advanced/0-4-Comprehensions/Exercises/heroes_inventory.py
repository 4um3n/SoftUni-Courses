heroes = {name: {} for name in input().split(", ")}
data = input()
while data != "End":
    name, item, cost = data.split("-")
    if item not in heroes[name]:
        heroes[name].update({item: int(cost)})

    data = input()

[print(f"{name} -> Items: {len(heroes[name])}, Cost: {sum(heroes[name].values())}") for name, items in heroes.items()]
