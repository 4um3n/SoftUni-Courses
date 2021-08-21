day = input()

twelve = ["Monday", "Tuesday", "Friday"]
fourteen = ["Wednesday", "Thursday"]
sixteen = ["Saturday", "Sunday"]

if day in twelve:
    print(f"12")
elif day in fourteen:
    print(f"14")
elif day in sixteen:
    print(f"16")
