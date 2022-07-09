def cache(function):
    cached_data = {}

    def wrapper(*args):
        if args not in cached_data:
            cached_data[args] = function(*args)
        return cached_data[args]

    return wrapper


@cache
def get_fib(n):
    if n < 2:
        return 1

    return get_fib(n - 1) + get_fib(n - 2)


print(get_fib(int(input())))
