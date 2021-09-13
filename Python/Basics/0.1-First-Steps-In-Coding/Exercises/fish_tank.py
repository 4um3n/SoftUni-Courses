length = int(input())
width = int(input())
height = int(input())
taken_space = float(input()) * 0.01
available_space = length * width * height * 0.001
needed_liters = available_space * (1 - taken_space)
print(needed_liters)
