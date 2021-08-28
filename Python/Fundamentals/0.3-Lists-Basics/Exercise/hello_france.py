items = input().split("|")
budget = float(input())
original_budget = budget
clothes_max_price = 50
shoes_max_price = 35
accessories_max_price = 20.50
prices = []

for index in range(len(items)):
    item_type, item_price = items[index].split("->")
    item_price = float(item_price)

    if item_type == "Clothes" and item_price > clothes_max_price:
        continue
    elif item_type == "Shoes" and item_price > shoes_max_price:
        continue
    elif item_type == "Accessories" and item_price > accessories_max_price:
        continue

    if item_price <= budget:
        budget -= item_price
        prices.append(item_price)

increased_prices = [prices[i] + prices[i] * 0.40 for i in range(len(prices))]
profit = sum(increased_prices) - sum(prices)
increased_prices = [f"{p:.2f}" for p in increased_prices]
print(" ".join(increased_prices))
print(f"Profit: {profit:.2f}")
original_budget += profit
if original_budget >= 150:
    print(f"Hello, France!")
else:
    print(f"Time to go.")
