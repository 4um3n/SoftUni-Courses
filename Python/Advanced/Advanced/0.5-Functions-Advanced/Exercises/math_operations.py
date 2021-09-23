def math_operations(*args, i=0, **kwargs):
    args = list(map(int, args))
    if not args:
        return kwargs

    if i == 0:
        res = kwargs['a'] + args[0]
        kwargs['a'] = res
        i += 1

    elif i == 1:
        res = kwargs['s'] - args[0]
        kwargs['s'] = res
        i += 1

    elif i == 2:
        if args[0] != 0:
            res = kwargs['d'] / args[0]
            kwargs['d'] = res

        i += 1

    elif i == 3:
        res = kwargs['m'] * args[0]
        kwargs['m'] = res
        i = 0

    return math_operations(*args[1:], i=i, **kwargs)
