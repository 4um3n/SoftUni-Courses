from collections import deque


def lsc(words):
    chain = [None] * len(words)
    sizes = [0] * len(words)
    best_size = 0
    best_idx = 0

    for idx in range(len(words)):
        current_word = words[idx]
        current_size = 0
        parent = None

        for prev_idx in range(idx - 1, -1, -1):
            prev_word = words[prev_idx]

            if len(current_word) <= len(prev_word):
                continue

            if current_size <= sizes[prev_idx] + 1:
                parent = prev_idx
                current_size = sizes[prev_idx] + 1

        chain[idx] = parent
        sizes[idx] = current_size

        if best_size < current_size:
            best_size = current_size
            best_idx = idx

    return chain, best_idx


def get_path(words, chain, best_idx):
    path = deque()

    while best_idx is not None:
        path.appendleft(words[best_idx])
        best_idx = chain[best_idx]

    return path


def main():
    words = input().split()
    chain, best_idx = lsc(words)
    return ' '.join(get_path(words, chain, best_idx))


if __name__ == '__main__':
    print(main())
