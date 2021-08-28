energy, coins = 100, 100
events = input().split("|")

for event_index in range(len(events)):
    event, event_value = events[event_index].split("-")
    event_value = int(event_value)

    if event == "rest":
        missing_energy = 100 - energy
        if event_value > missing_energy:
            event_value = missing_energy

        energy += event_value
        print(f"You gained {event_value} energy.\n"
              f"Current energy: {energy}.")

    elif event == "order":
        if energy < 30:
            energy += 50
            print(f"You had to rest!")
            continue
        
        coins += event_value
        energy -= 30
        print(f"You earned {event_value} coins.")

    else:
        coins -= event_value
        if coins <= 0:
            print(f"Closed! Cannot afford {event}.")
            exit()

        print(f"You bought {event}.")

print(f'Day completed!\n'
      f'Coins: {coins}\n'
      f'Energy: {energy}')

