degrees = int(input())
day_time = input()

outfit = ["Sweatshirt", "Shirt", "T-Shirt", "Swim Suit"]
shoes = ["Sneakers", "Moccasins", "Sandals", "Barefoot"]

if 10 <= degrees <= 18:
    if day_time == "Morning":
        outfit = outfit[0]
        shoes = shoes[0]
    elif day_time == "Afternoon":
        outfit = outfit[1]
        shoes = shoes[1]
    elif day_time == "Evening":
        outfit = outfit[1]
        shoes = shoes[1]
elif 18 < degrees <= 24:
    if day_time == "Morning":
        outfit = outfit[1]
        shoes = shoes[1]
    elif day_time == "Afternoon":
        outfit = outfit[2]
        shoes = shoes[2]
    elif day_time == "Evening":
        outfit = outfit[1]
        shoes = shoes[1]
elif degrees >= 25:
    if day_time == "Morning":
        outfit = outfit[2]
        shoes = shoes[2]
    elif day_time == "Afternoon":
        outfit = outfit[3]
        shoes = shoes[3]
    elif day_time == "Evening":
        outfit = outfit[1]
        shoes = shoes[1]

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
