def concatenate(*args, result=""):
    if not args:
        return result
    return concatenate(*args[1:], result=result+args[0])
