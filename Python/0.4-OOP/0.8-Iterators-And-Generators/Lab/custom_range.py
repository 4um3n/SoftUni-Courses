class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        self.current += 1
        return self.current - 1


a = custom_range(1, 14)
for i in a:
    print(i, end=' ')

print()
for i in a:
    print(i, end=' ')
