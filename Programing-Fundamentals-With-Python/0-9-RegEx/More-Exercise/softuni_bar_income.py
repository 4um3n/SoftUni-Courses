import re

pattern = r"%([A-Z][a-z]+)%[^\|\$\.%]*<([\w]+)>[^\|\$\.%]*\|(\d+)\|[^\|\$\.%\d]*(\d+\.?\d+)\$"
line, total_income = input(), 0
while line != "end of shift":
    line = re.findall(pattern, line)
    if line:
        customer, product, count, price = line[0]
        price = int(count) * float(price)
        print(f"{customer}: {product} - {price:.2f}")
        total_income += price
    
    line = input()

print(f"Total income: {total_income:.2f}")
