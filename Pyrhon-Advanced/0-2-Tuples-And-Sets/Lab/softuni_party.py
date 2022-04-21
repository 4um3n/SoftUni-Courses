vip_guests, regular_guests = set(), set()
for _ in range(int(input())):
    guest_code = input()
    if guest_code[0].isdigit():
        vip_guests.add(guest_code)
    else:
        regular_guests.add(guest_code)

guest = input()
while guest != "END":
    if guest in vip_guests:
        vip_guests.remove(guest)
    elif guest in regular_guests:
        regular_guests.remove(guest)

    guest = input()

print(len(vip_guests) + len(regular_guests))
[print(g) for g in sorted(vip_guests)]
[print(g) for g in sorted(regular_guests)]
