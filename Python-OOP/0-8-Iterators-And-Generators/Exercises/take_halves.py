def solution():
    def integers():
        # TODO: Implement
        n = 1
        while True:
            yield n
            n +=1

    def halves():
        # TODO: Implement
        for i in integers():
            yield i / 2

    def take(n, seq):
        # TODO: Implement
        res = []
        i = 0
        while i < n:
            res.append(next(seq))
            i += 1

        return res

    return take, halves, integers


take_func = solution()[0]
halves_data = solution()[1]
print(take_func(5, halves_data()))
