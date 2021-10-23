from collections import deque

wedding_materials = deque([int(n) for n in input().split()])
magic_levels = deque([int(n) for n in input().split()])
presents_data = {
    "Gemstone": {"range": range(100, 200), "count": 0},
    "Porcelain Sculpture": {"range": range(200, 300), "count": 0},
    "Gold": {"range": range(300, 400), "count": 0},
    "Diamond Jewellery": {"range": range(400, 500), "count": 0},
}

while wedding_materials and magic_levels:
    res = wedding_materials[-1] + magic_levels[0]

    if res < 100:
        if res % 2 == 0:
            wedding_materials[-1], magic_levels[0] = wedding_materials[-1] * 2, magic_levels[0] * 3
        else:
            wedding_materials[-1], magic_levels[0] = wedding_materials[-1] * 2, magic_levels[0] * 2

        res = wedding_materials[-1] + magic_levels[0]

    elif res > 499:
        res //= 2

    for key, values in presents_data.items():
        if res in values["range"]:
            presents_data[key]["count"] += 1

    wedding_materials.pop()
    magic_levels.popleft()

if presents_data["Gemstone"]["count"] and presents_data["Porcelain Sculpture"]["count"] or presents_data["Gold"]["count"] and presents_data["Diamond Jewellery"]["count"]:
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if wedding_materials:
    print(f"Materials left: {', '.join([str(n) for n in wedding_materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(n) for n in magic_levels])}")

for k, v in sorted(presents_data.items()):
    if v["count"]:
        print(f"{k}: {v['count']}")
