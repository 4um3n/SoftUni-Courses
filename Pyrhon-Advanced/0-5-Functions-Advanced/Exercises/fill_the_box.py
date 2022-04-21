def fill_the_box(height, length, width, *args, space=None):
    args = list(args)
    if space is None:
        space = int(height) * int(width) * int(length)

    if args[0] == "Finish":
        return f"There is free space in the box. You could put {space} more cubes."
    elif space - int(args[0]) <= 0:
        args[0] -= space
        return f"No more free space! You have {sum(map(int, args[:args.index('Finish')]))} more cubes."

    return fill_the_box(height, length, width, *args[1:], space=space - int(args[0]))
