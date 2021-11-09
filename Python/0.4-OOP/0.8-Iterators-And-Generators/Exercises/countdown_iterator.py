class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count
        self.current = self.count

    def __iter__(self):
        self.current = self.count
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration

        self.current -= 1
        return self.current + 1


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")