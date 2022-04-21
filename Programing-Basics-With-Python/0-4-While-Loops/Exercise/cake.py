cake_width = int(input())
cake_length = int(input())
cake_area = cake_length * cake_width
is_stop = False

while cake_area > 0:
    current_cake_pieces = input()

    if current_cake_pieces == "STOP":
        is_stop = True
        break

    current_cake_pieces = int(current_cake_pieces)
    cake_area -= current_cake_pieces

if is_stop and cake_area > 0:
    print(f"{cake_area} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")
