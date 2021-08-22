exam_hour = int(input())
exam_minutes = int(input())
coming_hour = int(input())
coming_minutes = int(input())

while exam_hour > 0:
    exam_minutes += 60
    exam_hour -= 1

while coming_hour > 0:
    coming_minutes += 60
    coming_hour -= 1

if coming_minutes > exam_minutes:
    print(f"Late")
    diff = abs(exam_minutes - coming_minutes)
    current_hour = 0
    current_minutes = 0

    if diff >= 1:
        if diff < 60:
            print(f"{diff} minutes after the start")
        else:
            while diff > 59:
                current_hour += 1
                diff -= 60
            current_minutes = diff
            if current_minutes >= 10:
                print(f"{current_hour}:{current_minutes} hours after the start")
            else:
                print(f"{current_hour}:0{current_minutes} hours after the start")

elif coming_minutes <= exam_minutes:
    diff = abs(exam_minutes - coming_minutes)
    if diff <= 30:
        print(f"On time")
    else:
        print(f"Early")

    current_hour = 0
    current_minutes = 0
    if diff >= 1:
        if diff < 60:
            print(f"{diff} minutes before the start")
        else:
            while diff > 59:
                current_hour += 1
                diff -= 60
            current_minutes = diff
            if current_minutes >= 10:
                print(f"{current_hour}:{current_minutes} hours before the start")
            else:
                print(f"{current_hour}:0{current_minutes} hours before the start")
