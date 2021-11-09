def fibonacci():
    current = 0
    previous = 1
    while True:
        yield current
        current = previous + current
        previous = current - previous


generator = fibonacci()
for i in range(10):
    print(next(generator))
