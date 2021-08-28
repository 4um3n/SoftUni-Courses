room_rent = float(input())
cake_price = room_rent * 0.20
drinks = cake_price - (cake_price * 0.45)
animator = room_rent / 3
needed_sum = cake_price + drinks + animator + room_rent
print(f"{needed_sum}")
