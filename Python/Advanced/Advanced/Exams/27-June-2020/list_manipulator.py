def list_manipulator(nums: list, *args):
    if "add" in args:
        if "beginning" in args:
            args = args[2:]
            nums, args = list(args), nums
            nums.extend(args)
        elif "end" in args:
            nums.extend(args[2:])

    elif "remove" in args:
        if "beginning" in args:
            args = args[2:]
            if args:
                [nums.pop(0) for _ in range(args[0]) if nums]
            else:
                nums.pop(0)

        elif "end" in args:
            args = args[2:]
            if args:
                [nums.pop() for _ in range(args[0]) if nums]
            else:
                nums.pop()

    return nums
