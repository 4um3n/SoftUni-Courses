people_count = int(input())
elevator_capacity = int(input())
courses_count = 0

while people_count > 0:
    people_count -= elevator_capacity
    courses_count += 1

print(courses_count)
