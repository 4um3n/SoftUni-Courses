products_prices = {
    "coffee": 1.50,
    "water": 1,
    "coke": 1.40,
    "snacks": 2
}
calculate_order = lambda product, count: products_prices[product] * count
print(f"{calculate_order(input(), int(input())):.2f}")
