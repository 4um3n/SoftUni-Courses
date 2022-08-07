from collections import deque


def lis(numbers):
    sizes = [0] * len(numbers)
    sizes[0] = 1

    parents = [None] * len(numbers)

    best_size = 1
    best_idx = 0

    for current_idx in range(1, len(numbers)):
        current_best_size = 1
        current_parent = None

        for prev_idx in range(current_idx - 1, -1, -1):
            if numbers[prev_idx] >= numbers[current_idx]:
                continue

            if sizes[prev_idx] + 1 >= current_best_size:
                current_best_size = sizes[prev_idx] + 1
                current_parent = prev_idx

        sizes[current_idx] = current_best_size
        parents[current_idx] = current_parent

        if current_best_size > best_size:
            best_size = current_best_size
            best_idx = current_idx

    return parents, best_idx


def get_path(numbers, parents, parent):
    path = deque()

    while parent is not None:
        path.appendleft(numbers[parent])
        parent = parents[parent]

    return path


def main():
    numbers = [int(n) for n in input().split()]
    parents, max_parent = lis(numbers)
    path = get_path(numbers, parents, max_parent)
    return ' '.join(str(n) for n in path)


if __name__ == '__main__':
    print(main())
