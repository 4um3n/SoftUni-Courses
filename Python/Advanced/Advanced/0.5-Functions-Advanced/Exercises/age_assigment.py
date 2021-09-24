def age_assignment(*args, result=dict(), **kwargs):
    if not args:
        return result

    result[args[0]] = kwargs[args[0][0]]
    return age_assignment(*args[1:], result=result, **kwargs)
