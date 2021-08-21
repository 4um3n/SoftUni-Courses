holiday_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = (int(input()))

puzzles_price = 2.6
dolls_price = 3
bears_price = 4.1
minions_price = 8.2
trucks_price = 2

total_puzzles_price = puzzles_price * puzzles_count
total_dolls_price = dolls_price * dolls_count
total_bears_price = bears_price * bears_count
total_minions_price = minions_price * minions_count
total_trucks_price = trucks_price * trucks_count

total_price = total_puzzles_price + total_minions_price + total_trucks_price + total_bears_price + total_dolls_price

total_toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

if total_toys_count >= 50:
    total_price = total_price - (total_price * 0.25)

rent_price = total_price * 0.1
remaining_sum = total_price - rent_price

if remaining_sum >= holiday_price:
    remaining_sum -= holiday_price
    print(f"Yes! {remaining_sum:.2f} lv left.")
else:
    needed_money = holiday_price - remaining_sum
    print(f"Not enough money! {needed_money:.2f} lv needed.")
