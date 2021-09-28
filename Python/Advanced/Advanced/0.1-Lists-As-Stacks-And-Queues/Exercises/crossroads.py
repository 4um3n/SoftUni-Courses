from collections import deque


def crossing_road(waiting_cars, free_wind_dur, green_light_dur, passed_cars=0):
    while waiting_cars and green_light_dur > 0:
        current_car = deque(waiting_cars[0])
        while current_car:
            if green_light_dur:
                green_light_dur -= 1
            elif free_wind_dur:
                free_wind_dur -= 1
            else:
                print(f"A crash happened!\n"
                      f"{waiting_cars[0]} was hit at {current_car[0]}.")
                exit()

            current_car.popleft()

        waiting_cars.popleft()
        passed_cars += 1

    return waiting_cars, passed_cars


def anticipate_the_situation(free_wind_dur, green_light_dur, waiting_cars=deque(), total_passed_cars=0):
    car = input()
    while car != "END":
        if car == "green":
            waiting_cars, passed_cars = crossing_road(waiting_cars, free_wind_dur, green_light_dur)
            total_passed_cars += passed_cars
        else:
            waiting_cars.append(car)
        car = input()

    return f"Everyone is safe.\n" \
           f"{total_passed_cars} total cars passed the crossroads."


green_light_duration = int(input())
free_window_duration = int(input())
print(anticipate_the_situation(free_window_duration, green_light_duration))
