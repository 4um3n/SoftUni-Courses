import re

pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"
command, products, total_price = input(), [], 0
while command != "Purchase":
    match = re.findall(pattern, command)
    for m in match:
        products.append(m[0])
        total_price += float(m[1]) * int(m[2])
    
    command = input()

print(f"Bought furniture:")
if products:
    print('\n'.join(products))
print(f"Total money spend: {total_price:.2f}")
