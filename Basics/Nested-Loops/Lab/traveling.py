destination = input()

while destination != "End":
    destination_price = float(input())
    saved_money = 0

    while saved_money < destination_price:
        current_saving_money = float(input())
        saved_money += current_saving_money

    print(f"Going to {destination}!")
    destination = input()
