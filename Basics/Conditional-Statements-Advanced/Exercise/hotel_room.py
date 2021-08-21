month = input()
nights_count = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights_count <= 14:
        studio_price -= studio_price * 0.05
    elif nights_count > 14:
        studio_price -= studio_price * 0.30
        apartment_price -= apartment_price * 0.10
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights_count > 14:
        studio_price -= studio_price * 0.20
        apartment_price -= apartment_price * 0.10
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights_count > 14:
        apartment_price -= apartment_price * 0.10

apartment_sum = apartment_price * nights_count
studio_sum = studio_price * nights_count

print(f"Apartment: {apartment_sum:.2f} lv.")
print(f"Studio: {studio_sum:.2f} lv.")
