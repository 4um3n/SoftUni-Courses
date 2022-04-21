products = {}
command = input()
while command != "buy":
    product, price, quantity = command.split()
    if product not in products:
        products[product] = {"price": 0, "quantity": 0}
    
    products[product]["price"] = float(price)
    products[product]["quantity"] += int(quantity)
    command = input()
    
for p, v in products.items():
    print(f"{p} -> {(v['price'] * v['quantity']):.2f}")
