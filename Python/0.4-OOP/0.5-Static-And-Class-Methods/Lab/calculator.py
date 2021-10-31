from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y if x != 0 and y != 0 else 1, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)
