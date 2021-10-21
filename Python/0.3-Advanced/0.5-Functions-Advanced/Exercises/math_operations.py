def math_operations(*args, i=None, **kwargs):
    if i is None:
        i = 0
        args = tuple(map(int, args))

    if not args:
        return kwargs

    if i == 0:
        res = kwargs['a'] + args[0]
        kwargs['a'] = res

    elif i == 1:
        res = kwargs['s'] - args[0]
        kwargs['s'] = res

    elif i == 2:
        if args[0] != 0:
            res = kwargs['d'] / args[0]
            kwargs['d'] = res

    elif i == 3:
        res = kwargs['m'] * args[0]
        kwargs['m'] = res

    return math_operations(*args[1:], i=0 if i == 3 else i+1, **kwargs)
