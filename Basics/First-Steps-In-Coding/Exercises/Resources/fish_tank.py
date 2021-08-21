length = int(input())
width = int(input())
height = int(input())
taken_space = float(input())
taken_space_in_percents = taken_space * 0.01

available_space_in_centimeters = length * width * height
available_space_in_meters = available_space_in_centimeters * 0.001

needed_liters = available_space_in_meters * (1 - taken_space_in_percents)
print(needed_liters)
