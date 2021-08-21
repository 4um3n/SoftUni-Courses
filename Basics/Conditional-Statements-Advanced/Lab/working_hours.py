hour = int(input())
day = input()

working = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day in working:
    if 10 <= hour <= 18:
        print(f"open")
    else:
        print(f"closed")
else:
    print(f"closed")
