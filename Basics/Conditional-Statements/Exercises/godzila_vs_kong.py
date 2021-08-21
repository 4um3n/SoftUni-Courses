film_budget = float(input())
statists_count = int(input())
statist_clothes_price = float(input())

movie_decor = film_budget * 0.10
total_clothes_price = statists_count * statist_clothes_price

if statists_count > 150:
    total_clothes_price -= total_clothes_price * 0.10

end_price = total_clothes_price + movie_decor

diff = abs(film_budget - end_price)
if end_price > film_budget:
    print(f"Not enough money!\n"
    f"Wingard needs {diff:.2f} leva more.")
else:
    print(f"Action!\n"
          f"Wingard starts filming with {diff:.2f} leva left.")
