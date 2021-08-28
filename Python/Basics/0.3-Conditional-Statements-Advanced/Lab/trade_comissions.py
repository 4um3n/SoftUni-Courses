town = input()
sell_volume = float(input())
is_town_valid = False
is_sell_volume_valid = True
commission = 0

if sell_volume < 0:
    is_sell_volume_valid = False

if town == "Sofia":
    is_town_valid = True
    if 0 <= sell_volume <= 500:
        commission = 0.05
    elif 500 < sell_volume <= 1000:
        commission = 0.07
    elif 1000 < sell_volume <= 10000:
        commission = 0.08
    elif sell_volume > 10000:
        commission = 0.12
elif town == "Varna":
    is_town_valid = True
    if 0 <= sell_volume <= 500:
        commission = 0.045
    elif 500 < sell_volume <= 1000:
        commission = 0.075
    elif 1000 < sell_volume <= 10000:
        commission = 0.1
    elif sell_volume > 10000:
        commission = 0.13
elif town == "Plovdiv":
    is_town_valid = True
    if 0 <= sell_volume <= 500:
        commission = 0.055
    elif 500 < sell_volume <= 1000:
        commission = 0.08
    elif 1000 < sell_volume <= 10000:
        commission = 0.12
    elif sell_volume > 10000:
        commission = 0.145

end_result = sell_volume * commission

if is_town_valid and is_sell_volume_valid:
    print(f"{end_result:.2f}")
else:
    print(f"error")
