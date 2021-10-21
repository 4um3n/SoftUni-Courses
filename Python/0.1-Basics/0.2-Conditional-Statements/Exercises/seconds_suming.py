import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

minutes = total_time / 60
seconds = total_time % 60

minutes = math.floor(minutes)

if seconds >= 10:
    print(f"{minutes}:{seconds}")
else:
    print(f"{minutes}:0{seconds}")
