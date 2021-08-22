num = int(input())

bonus_points = 0
if num <= 100:
    bonus_points += 5
elif 1000 >= num > 100:
    bonus_points += num * 0.2
else:
    bonus_points += num * 0.1

even_bonus_points = 0
if num % 2 == 0:
    even_bonus_points += 1

five_ending_bonus_points = 0
if num % 10 == 5:
    five_ending_bonus_points += 2

total_bonus_points = bonus_points + even_bonus_points + five_ending_bonus_points
total_points = num + total_bonus_points

print(total_bonus_points)
print(total_points)