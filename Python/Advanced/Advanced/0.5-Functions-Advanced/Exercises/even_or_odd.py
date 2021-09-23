def even_odd(*args, result=None):
    if args and result is None:
        args = list(args)
        command = args.pop()
        if command == "even":
            args = list(filter(lambda x: x % 2 == 0, args))
        else:
            args = list(filter(lambda x: x % 2 == 1, args))

        result = []

    if not args:
        return result

    result.append(args[0])
    return even_odd(*args[1:], result=result)
