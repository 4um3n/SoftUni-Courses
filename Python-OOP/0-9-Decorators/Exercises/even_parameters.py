def even_parameters(function):
    def wrapper(*args, **kwargs):
        if all([isinstance(n, int) and n % 2 == 0 for n in args]):
            return function(*args, **kwargs)
        return f"Please use only even numbers!"
    return wrapper


# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
