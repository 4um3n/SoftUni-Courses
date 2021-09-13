from collections import deque


def crossing_road(cars: deque, gld: int, fwd: int):
    passed_cars = 0
    while cars and gld > 0:
        current_car = deque(cars[0])
        while current_car:
            if gld > 0:
                gld -= 1
                current_car.popleft()
            elif fwd > 0:
                fwd -= 1
                current_car.popleft()
            else:
                print(f"A crash happened!\n"
                      f"{cars[0]} was hit at {current_car[0]}.")
                exit()

        cars.popleft()
        passed_cars += 1

    return cars, passed_cars


green_light_duration = int(input())
free_window_duration = int(input())
total_passed_cars = 0
waiting_cars = deque()
car = input()
while car != "END":
    if car == "green":
        waiting_cars, current_passed_cars = crossing_road(waiting_cars, green_light_duration, free_window_duration)
        total_passed_cars += current_passed_cars
    else:
        waiting_cars.append(car)
    car = input()

print(f"Everyone is safe.\n"
      f"{total_passed_cars} total cars passed the crossroads.")
