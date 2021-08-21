import  sys

numbers_count = int(input())
biggest_number = -sys.maxsize
lowest_number = sys.maxsize

for num in range(numbers_count):
    current_number = int(input())

    if current_number > biggest_number:
        biggest_number = current_number

    if current_number < lowest_number:
        lowest_number = current_number

print(f"Max number: {biggest_number}")
print(f"Min number: {lowest_number}")
