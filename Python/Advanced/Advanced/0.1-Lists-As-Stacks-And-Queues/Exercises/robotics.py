from collections import deque
from datetime import datetime, timedelta


def change_overall_time(time):
    time += timedelta(seconds=1)
    return time


def next_available_time(time, rob):
    global initial_times
    time += timedelta(seconds=initial_times[rob])
    return time


data = [d.split("-") for d in input().split(";")]
initial_times = {r[0]: int(r[1]) for r in data}
current_time = datetime.strptime(input(), '%H:%M:%S')
robots = {r: current_time for r in initial_times}
available_robots = deque()
products = deque()
product = input()
while product != "End":
    products.append(product)
    product = input()

while products:
    current_time = change_overall_time(current_time)
    product = products.popleft()
    if not available_robots:
        for r in robots:
            if robots[r] <= current_time:
                available_robots.append(r)

    if available_robots:
        robot = available_robots.popleft()
        robots[robot] = next_available_time(current_time, robot)
        print(f"{robot} - {product} [{current_time.strftime('%H:%M:%S')}]")
    else:
        products.append(product)
