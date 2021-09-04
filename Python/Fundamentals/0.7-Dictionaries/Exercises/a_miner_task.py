resource, items = input(), {}
while resource != "stop":
    quantity = int(input())
    if resource not in items:
        items[resource] = 0
    
    items[resource] += quantity
    resource = input()

for r, q in items.items():
    print(f"{r} -> {q}")
