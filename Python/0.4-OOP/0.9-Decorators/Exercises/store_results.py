class store_results:
    _log_file = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open(self._log_file, 'a') as file:
            result = self.function(*args, **kwargs)
            file.write(f"Function '{self.function.__name__}' was called. Result: {result}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 5)