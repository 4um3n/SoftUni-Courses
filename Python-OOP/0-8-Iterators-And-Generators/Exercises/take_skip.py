class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        # self.current = [n for n in range(0, self.count * self.step, self.step)]
        self.number = 0

    def __iter__(self):
        # self.current = [n for n in range(0, self.count * self.step, self.step)]
        # self.number = 0
        return self

    def __next__(self):
        if self.number > (self.count - 1) * self.step:
            raise StopIteration

        self.number += self.step
        return self.number - self.step

        # if not self.current:
        #     raise StopIteration
        #
        # return self.current.pop(0)


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
