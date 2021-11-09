class dictionary_iter:
    def __init__(self, dictionary_obj: dict) -> None:
        self.dictionary = dictionary_obj
        # self.items = tuple(self.dictionary.items())
        self.items = iter(self.dictionary.items())
        self.index = 0

    def __iter__(self):
        # self.index = 0
        return self

    def __next__(self):
        # if self.index >= len(self.items):
        #     raise StopIteration

        # self.index += 1
        return next(self.items)


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

for x in result:
    print(x)
