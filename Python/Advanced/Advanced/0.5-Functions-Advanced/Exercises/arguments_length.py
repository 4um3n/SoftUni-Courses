def args_length(*args):
    if args:
        return args_length(*args[1:]) + 1
    return 0
