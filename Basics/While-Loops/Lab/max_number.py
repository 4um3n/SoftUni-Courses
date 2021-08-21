import sys

number = input()
max_number = -sys.maxsize

while number != "Stop":
    number = int(number)

    if max_number < number:
        max_number = number

    number = input()

print(f"{max_number}")
