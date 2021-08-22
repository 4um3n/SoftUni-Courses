snowballs_count = int(input())
best_snowball_value = 0
best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0

for snowball in range(snowballs_count):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality


print(f"{best_snowball_snow} : {best_snowball_time} = {int(best_snowball_value)} ({best_snowball_quality})")

