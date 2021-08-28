speed = float(input())

if speed <= 10:
    print(f"slow")
elif speed <= 50:
    print(f"average")
elif speed <= 150:
    print(f"fast")
elif speed <= 1000:
    print(f"ultra fast")
else:
    print(f"extremely fast")
