def even_odd(*args, result=None):
    if result is None and args:
        result = list()
        args = tuple(filter(lambda x: x % 2 == 1 if args[-1] == "odd" else x % 2 == 0, args[:-1]))

    if not args:
        return result

    result.append(args[0])
    return even_odd(*args[1:], result=result)
