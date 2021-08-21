free_room_width = int(input())
free_room_length = int(input())
free_room_height = int(input())
free_room_area = free_room_width * free_room_length * free_room_height
is_room_space_end = False
current_boxes_count = input()

while current_boxes_count != "Done":
    current_boxes_count = int(current_boxes_count)

    if free_room_area <= current_boxes_count:
        is_room_space_end = True
        break

    free_room_area -= current_boxes_count
    current_boxes_count = input()

if is_room_space_end:
    print(f"No more free space! You need {abs(free_room_area - current_boxes_count)} Cubic meters more.")
else:
    print(f"{free_room_area} Cubic meters left.")
