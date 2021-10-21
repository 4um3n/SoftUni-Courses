hour = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    minutes -= 60
    hour += 1

if hour >= 24:
    hour -= 24

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
