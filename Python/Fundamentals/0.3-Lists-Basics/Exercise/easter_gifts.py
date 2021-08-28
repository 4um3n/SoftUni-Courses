gifts = input().split()

command = input()
while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        gift = command[1]

        for index in range(len(gifts)):
            if gifts[index] == gift:
                gifts[index] = "None"

    elif "Required" in command:
        gift, gift_i = command[1], int(command[2])

        if 0 <= gift_i < len(gifts):
            gifts[gift_i] = gift

    elif "JustInCase" in command:
        gift = command[1]
        gifts[-1] = gift

    command = input()

gifts = [g for g in gifts if g != "None"]
print(" ".join(gifts))
