def func_executor(*args, result=None):
    if result is None:
        result = list()

    if not args:
        return result

    func = args[0][0]
    arguments = args[0][1]
    result.append(func(*arguments))
    return func_executor(*args[1:], result=result)


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
