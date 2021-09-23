def concatenate(*args, result=""):
    if args:
        return concatenate(*args[1:], result=result+args[0])

    return result
