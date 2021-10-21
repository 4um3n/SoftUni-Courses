products = input().split()
products = {products[i]: int(products[i + 1]) for i in range(0, len(products), 2)}
for p in input().split():
    if p in products:
        print(f"We have {products[p]} of {p} left")
        continue

    print(f"Sorry, we don't have {p}")