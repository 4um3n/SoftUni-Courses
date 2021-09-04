command, products = input(), {}
while command != "statistics":
    p, q = command.split(": ")
    if p not in products:
        products[p] = 0
    
    products[p] += int(q)
    command = input()

print(F"Products in stock:")
for p, q in products.items():
    print(f"- {p}: {q}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")