budget = int(input())
season = input()
fishers_count = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
    if fishers_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif 7 <= fishers_count <= 11:
        boat_rent -= boat_rent * 0.15
    elif fishers_count >= 12:
        boat_rent -= boat_rent * 0.25
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
    if fishers_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif 7 <= fishers_count <= 11:
        boat_rent -= boat_rent * 0.15
    elif fishers_count >= 12:
        boat_rent -= boat_rent * 0.25
elif season == "Winter":
    boat_rent = 2600
    if fishers_count <= 6:
        boat_rent -= boat_rent * 0.10
    elif 7 <= fishers_count <= 11:
        boat_rent -= boat_rent * 0.15
    elif fishers_count >= 12:
        boat_rent -= boat_rent * 0.25

if not season == "Autumn":
    if fishers_count % 2 == 0:
        boat_rent -= boat_rent * 0.05

money_left_or_needed = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {money_left_or_needed:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left_or_needed:.2f} leva.")
