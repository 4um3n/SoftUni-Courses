from fibonacci import *

nums = []
command = input()
while command != "Stop":
    command = command.split()
    n = int(command[-1])

    if "Create" in command:
        nums = create_sequence(n)
        print(nums)

    elif "Locate" in command:
        print(locate_number(nums, n))

    command = input()
