def logged(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"you called {function.__name__}({', '.join([str(char) for char in args])})\n" \
               f"it returned {result}"

    return wrapper


# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
