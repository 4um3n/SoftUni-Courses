campaign_days_count = int(input())
chefs_count = int(input())
cakes_per_chef = int(input())
waffles_per_chef = int(input())
pancakes_per_chef = int(input())

cakes_price_day = cakes_per_chef * 45
waffles_price_day = waffles_per_chef * 5.80
pancakes_price_day = pancakes_per_chef * 3.20
total_sum_day = (cakes_price_per_day + waffles_price_per_day + pancakes_price_per_day) * chefs_count
total_sum_campaign = total_sum_per_day * campaign_days_count
total_sum_campaign -= total_sum_per_campaign / 8
print(f"{total_sum_per_campaign}")
