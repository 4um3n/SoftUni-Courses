from collections import deque


class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance


def get_graph(edges):
    graph = []
    for _ in range(edges):
        source, destination, distance = [int(x) for x in input().split(' ')]
        graph.append(Edge(source, destination, distance))

    return graph


def get_path(destination, parents):
    path = deque([destination])
    node = parents[destination]

    while node is not None:
        path.appendleft(node)
        node = parents[node]

    return path


def bellman_ford(nodes, start, graph):
    parents = [None] * (nodes + 1)
    distances = [float('inf')] * (nodes + 1)
    distances[start] = 0
    cyclical = False

    for _ in range(nodes):
        updated = False

        for edge in graph:
            if distances[edge.source] == float('inf'):
                continue

            new_distance = distances[edge.source] + edge.weight
            if new_distance < distances[edge.destination]:
                distances[edge.destination] = new_distance
                parents[edge.destination] = edge.source
                updated = True

        if not updated:
            break

    for edge in graph:
        new_distance = distances[edge.source] + edge.weight
        if new_distance < distances[edge.destination]:
            cyclical = True
            break

    return parents, distances, cyclical


def main():
    nodes = int(input())
    edges = int(input())
    graph = get_graph(edges)
    start = int(input())
    destination = int(input())
    parents, distances, cyclical = bellman_ford(nodes, start, graph)

    if cyclical:
        return 'Negative Cycle Detected'

    path = ' '.join([str(x) for x in get_path(destination, parents)])
    return '\n'.join([
        path,
        str(distances[destination])
    ])


if __name__ == '__main__':
    print(main())
