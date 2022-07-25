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


def bellman_ford(nodes_count, source, graph):
    parents = [None] * (nodes_count + 1)
    distances = [float('inf')] * (nodes_count + 1)
    distances[source] = 0
    cyclical = False

    for _ in range(nodes_count):
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


def get_path(destination, parents):
    path = deque([destination])
    node = parents[destination]

    while node is not None:
        path.appendleft(node)
        node = parents[node]

    return path


def main():
    nodes_count = int(input())
    edges_count = int(input())
    graph = get_graph(edges_count)
    source = int(input())
    destination = int(input())
    parents, distances, cyclical = bellman_ford(nodes_count, source, graph)

    if cyclical:
        return 'Undefined'

    path = get_path(destination, parents)
    return '\n'.join([
        ' '.join([str(n) for n in path]),
        str(distances[destination])
    ])


if __name__ == '__main__':
    print(main())
