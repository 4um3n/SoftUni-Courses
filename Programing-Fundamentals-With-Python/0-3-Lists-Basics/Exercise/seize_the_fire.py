fire_cells = input().split("#")
amount_of_water = int(input())
high_fire = range(81, 126)
medium_fire = range(51, 81)
low_fire = range(1, 51)
total_effort, total_fire, cells_out = 0, 0, []

for index in range(len(fire_cells)):
    current_fire = fire_cells[index].split()
    type_of_fire = current_fire[0]
    cell_value = int(current_fire[len(current_fire) - 1])

    if type_of_fire == "High" and cell_value not in high_fire:
        continue
    elif type_of_fire == "Medium" and cell_value not in medium_fire:
        continue
    elif type_of_fire == "Low" and cell_value not in low_fire:
        continue

    if cell_value <= amount_of_water:
        amount_of_water -= cell_value
        total_effort += cell_value * 0.25
        total_fire += cell_value
        cells_out.append(cell_value)
    
    if amount_of_water == 0:
        break

print("Cells:")
for i in range(len(cells_out)):
    print(f" - {cells_out[i]}")

print(f"Effort: {total_effort:.2f}\n"
      f"Total Fire: {total_fire}")
