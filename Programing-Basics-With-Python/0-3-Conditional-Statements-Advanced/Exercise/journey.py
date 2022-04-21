budget = float(input())
season = input()
destination = ""
spent_money = 0
holiday_type = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.30
        holiday_type = "Camp"
    elif season == "winter":
        spent_money = budget * 0.70
        holiday_type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.40
        holiday_type = "Camp"
    elif season == "winter":
        spent_money = budget * 0.80
        holiday_type = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent_money = budget * 0.90
    holiday_type = "Hotel"

print(f"Somewhere in {destination}\n"
      f"{holiday_type} - {spent_money:.2f}")
