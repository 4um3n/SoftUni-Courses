from collections import deque

materials_boxes = deque([int(n) for n in input().split()])
magic_values = deque([int(n) for n in input().split()])
toys_values = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
toys = []
while materials_boxes and magic_values:
    if materials_boxes[-1] == 0 or magic_values[0] == 0:
        if materials_boxes[-1] == 0:
            materials_boxes.pop()
        if magic_values[0] == 0:
            magic_values.popleft()
        continue

    box = materials_boxes.pop()
    magic = magic_values.popleft()
    result = box * magic

    if result in toys_values:
        toys.append(toys_values[result])
    elif result < 0:
        result = box + magic
        materials_boxes.append(result)
    else:
        materials_boxes.append(box + 15)


if "Doll" in toys and "Wooden train" in toys or "Teddy bear" in toys and "Bicycle" in toys:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials_boxes:
    materials_boxes = [str(n) for n in materials_boxes][::-1]
    print(f"Materials left: {', '.join(materials_boxes)}")

if magic_values:
    magic_values = [str(n) for n in magic_values]
    print(f"Magic left: {', '.join(magic_values)}")

[print(f"{toy}: {toys.count(toy)}") for toy in sorted(set(toys))]
