class reverse_iter:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.index = len(self.iterable) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            # self.index = len(self.iterable) - 1
            raise StopIteration

        self.index -= 1
        return self.iterable[self.index + 1]

    def __repr__(self):
        iter_to_str = ', '.join([str(el) for el in self.iterable[::-1]])
        return f"[{iter_to_str}]"


a = range(14)
reversed_a = reverse_iter(a)
print(reversed_a)
for elem in reversed_a:
    print(elem, end=' ')

for elem in reversed_a:
    print(elem, end=' ')
