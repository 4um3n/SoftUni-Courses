from collections import deque


def get_graph(edges_count):
    graph = {}

    for _ in range(edges_count):
        source, destination = [int(x) for x in input().split()]

        if source not in graph:
            graph[source] = []

        if destination not in graph:
            graph[destination] = []

        graph[source].append(destination)

    return graph


def get_parents(start, destination, graph):
    parents = {}
    visited = set()
    nodes_queue = deque([start])

    while nodes_queue:
        parent = nodes_queue.popleft()

        for child in graph[parent]:
            if child in visited:
                continue

            visited.add(child)
            parents[child] = parent
            nodes_queue.append(child)

            if child == destination:
                break

    return parents


def get_path(parents, destination):
    path = deque([destination])
    parent = parents.get(destination)

    while parent is not None:
        path.appendleft(parent)
        parent = parents.get(parent)

    return path


def main():
    nodes_count = int(input())
    edges_count = int(input())
    edges = get_graph(edges_count)
    start = int(input())
    destination = int(input())

    parents = get_parents(start, destination, edges)
    path = " ".join([str(x) for x in get_path(parents, destination)])
    return f'Shortest path length is: {len(path) - 1}\n' \
           f'{path}'


if __name__ == '__main__':
    print(main())
