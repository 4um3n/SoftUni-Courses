command = input()
coffee_count = 0
lower_cases = ["coding", "cat", "dog", "movie"]
upper_cases = []

for i in lower_cases:
    i = i.upper()
    upper_cases.append(i)

while command != "END":

    if command in lower_cases:
        coffee_count += 1
    elif command in upper_cases:
        coffee_count += 2

    command = input()

if coffee_count > 5:
    print(f"You need extra sleep")
else:
    print(f"{coffee_count}")
