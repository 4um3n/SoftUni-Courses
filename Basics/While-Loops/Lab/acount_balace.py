command = input()
balance = 0

while command != "NoMoreMoney":
    command = float(command)

    if command < 0:
        print(f"Invalid operation!")
        break

    balance += command
    print(f"Increase: {command:.2f}")
    command = input()

print(f"Total: {balance:.2f}")
