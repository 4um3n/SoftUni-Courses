stay_days = int(input())
room_kind = input()
appraisal = input()
nights = stay_days - 1
discount = 0
end_sum = 0

if room_kind == "room for one person":
    room_price = 18
    end_sum = room_price * nights
elif room_kind == "apartment":
    room_price = 25
    end_sum = room_price * nights
    if stay_days < 10:
        discount = end_sum * 0.30
    elif stay_days <= 15:
        discount = end_sum * 0.35
    elif stay_days > 15:
        discount = end_sum * 0.50
elif room_kind == "president apartment":
    room_price = 35
    end_sum = room_price * nights
    if stay_days < 10:
        discount = end_sum * 0.10
    elif stay_days <= 15:
        discount = end_sum * 0.15
    elif stay_days > 15:
        discount = end_sum * 0.20

end_sum -= discount

if appraisal == "positive":
    end_sum += end_sum * 0.25
else:
    end_sum -= end_sum * 0.10

print(f"{end_sum:.2f}")
