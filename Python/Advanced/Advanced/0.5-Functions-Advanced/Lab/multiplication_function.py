def multiply(result=1, *args):
    if not args:
        return result

    return multiply(result * args[0], *args[1:])
