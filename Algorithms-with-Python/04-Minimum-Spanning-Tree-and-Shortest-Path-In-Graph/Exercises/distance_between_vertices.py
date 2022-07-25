from collections import deque


def get_graph(nodes_count):
    graph = {}

    for _ in range(nodes_count):
        source, children = input().split(':')
        source = int(source)
        children = [int(n) for n in children.split()]

        if source not in graph:
            graph[source] = []

        graph[source].extend(children)

    return graph


def get_pairs(pairs_count):
    pairs = []

    for _ in range(pairs_count):
        pairs.append([int(n) for n in input().split('-')])

    return pairs


def bfs(source, destination, graph):
    parents = {}
    waiting_nodes = deque([source])

    while waiting_nodes:
        node = waiting_nodes.popleft()

        if node == destination:
            break

        for child in graph[node]:
            if child in parents:
                continue

            parents[child] = node
            waiting_nodes.append(child)

    return parents


def get_distance(source, destination, parents):
    distance = 0
    node = parents.get(destination)

    while node is not None:
        distance += 1

        if node == source:
            break

        node = parents.get(node)

    return distance


def get_distances(pairs, graph):
    distances = deque()

    for source, destination in pairs:
        parents = bfs(source, destination, graph)
        distance = -1

        if destination in parents:
            distance = get_distance(source, destination, parents)

        distances.append((source, destination, distance))

    return distances


def main():
    nodes_count = int(input())
    pairs_count = int(input())
    graph = get_graph(nodes_count)
    pairs = get_pairs(pairs_count)
    distances = get_distances(pairs, graph)

    message = [f'{{{sour}, {dest}}} -> {dist}' for sour, dest, dist in distances]
    return '\n'.join(message)


if __name__ == '__main__':
    print(main())
