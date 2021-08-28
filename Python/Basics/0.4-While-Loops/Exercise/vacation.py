needed_money = float(input())
current_money = float(input())
total_days_counter = 0
spend_days_counter = 0
is_spend_five = False

while current_money < needed_money:
    total_days_counter += 1
    action_kind = input()
    action_money = float(input())

    if action_kind == "spend":
        if action_money > current_money:
            action_money = current_money

        spend_days_counter += 1
        current_money -= action_money

    elif action_kind == "save":
        spend_days_counter = 0
        current_money += action_money

    if spend_days_counter >= 5:
        is_spend_five = True
        break

if is_spend_five:
    print(f"You can't save the money.\n"
          f"{total_days_counter}")
else:
    print(f"You saved the money for {total_days_counter} days.")
