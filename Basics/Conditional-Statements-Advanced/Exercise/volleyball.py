import math

year_type = input()
holiday_count = int(input())
hometown_weekend_count = int(input())
normal_weekend_count = 48 - hometown_weekend_count

normal_games = normal_weekend_count * 3/4
hometown_games = hometown_weekend_count
holiday_games = holiday_count * 2/3
total_games = normal_games + hometown_games + holiday_games

if year_type == "leap":
    total_games += total_games * 0.15

total_games = math.floor(total_games)

print(total_games)
