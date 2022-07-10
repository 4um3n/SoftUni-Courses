def get_solutions(ind: int, target: str, words_by_ind: dict, words_count: dict, used_words=[]):
    if ind >= len(target):
        print(' '.join(used_words))
        return

    if ind not in words_by_ind:
        return

    for word in words_by_ind[ind]:
        if words_count[word] == 0:
            continue

        used_words.append(word)
        words_count[word] -= 1
        get_solutions(ind + len(word), target, words_by_ind, words_count, used_words)
        words_count[word] += 1
        used_words.pop()


def get_words_mappers(words, target):
    words_by_ind = {}
    words_count = {}

    for word in words:
        if word in words_count:
            words_count[word] += 1
            continue

        words_count[word] = 1

        try:
            ind = 0
            while True:
                ind = target.index(word, ind)

                if ind not in words_by_ind:
                    words_by_ind[ind] = []

                words_by_ind[ind].append(word)
                ind += len(word)
        except ValueError:
            pass

    return words_by_ind, words_count


def main():
    words = input().split(', ')
    target = input()
    get_solutions(0, target, *get_words_mappers(words, target))


if __name__ == '__main__':
    main()
