from time import time


def exec_time(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)
        end_time = time()
        return end_time - start_time
    return wrapper


# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total


# print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
