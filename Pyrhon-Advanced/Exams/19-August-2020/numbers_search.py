def numbers_searching(*args, missing_n=None, res=None):
    if not args:
        res.sort()
        return [missing_n, res]

    if res is None:
        high, low, res = max(args), min(args), []
        missing_numbers = [n for n in range(low, high) if n not in args]
        if missing_numbers:
            missing_n = missing_numbers[-1]

    if args.count(args[0]) > 1 and args[0] not in res:
        res.append(args[0])

    return numbers_searching(*args[1:], missing_n=missing_n, res=res)
