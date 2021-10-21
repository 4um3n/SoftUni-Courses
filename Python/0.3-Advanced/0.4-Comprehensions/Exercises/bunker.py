items_categories = {c: {} for c in input().split(", ")}
for _ in range(int(input())):
    category, item, items_data = input().split(" - ")
    quantity = int(items_data.split(";")[0].split(":")[1])
    quality = int(items_data.split(";")[1].split(":")[1])

    if item not in items_categories[category]:
        items_categories[category][item] = {"quantity": 0, "quality": 0}
        items_categories[category][item]['quantity'] += int(quantity)
        items_categories[category][item]['quality'] += int(quality)

print(sum(items_categories[c][i]["quantity"] for c in items_categories for i in items_categories[c]))
qualities = [sum([items_categories[c][i]["quality"] for i in items_categories[c]]) for c in items_categories]
print(f"Average quality: {sum(qualities) / len(qualities):.2f}")
print('\n'.join([f"{c} -> {', '.join([i for i in items_categories[c]])}" for c in items_categories]))
