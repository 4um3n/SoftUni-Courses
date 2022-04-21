class sequence_repeat:
    def __init__(self, sequence: iter, number: int) -> None:
        self.sequence = sequence
        self.count = number
        self.counter = 0
        self.index = 0

    def __iter__(self):
        # self.index = 0
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration

        if self.index >= len(self.sequence):
            self.index = 0

        self.counter += 1
        self.index += 1
        return self.sequence[self.index - 1]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
