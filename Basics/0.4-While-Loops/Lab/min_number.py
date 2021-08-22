import sys

number = input()
min_number = sys.maxsize

while number != "Stop":
    number = int(number)

    if min_number > number:
        min_number = number

    number = input()

print(f"{min_number}")
