from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance


def get_graph():
    graph = {}

    for _ in range(int(input())):
        source, destination, distance = [int(x) for x in input().split(', ')]

        if source not in graph:
            graph[source] = []

        if destination not in graph:
            graph[destination] = []

        graph[source].append(Edge(source, destination, distance))

    return graph


def get_path(destination, parents):
    path = deque([destination])
    parent = parents[destination]

    while parent is not None:
        path.appendleft(parent)
        parent = parents[parent]

    return path


def dijkstra(start, destination, graph):
    max_node = max(graph.keys())
    parents = [None] * (max_node + 1)
    distances = [float('inf')] * (max_node + 1)
    distances[start] = 0

    distances_pq = PriorityQueue()
    distances_pq.put((0, start))

    while not distances_pq.empty():
        min_distance, node = distances_pq.get()

        if node == destination:
            break

        for edge in graph[node]:
            child = edge.destination
            current_distance = edge.price + min_distance

            if current_distance < distances[child]:
                parents[child] = node
                distances[child] = current_distance
                distances_pq.put((current_distance, child))

    return parents, distances


def main():
    graph = get_graph()
    start = int(input())
    destination = int(input())
    parents, distances = dijkstra(start, destination, graph)

    if distances[destination] == float('inf'):
        return 'There is no such path.'

    path = ' '.join([str(x) for x in get_path(destination, parents)])
    return f'{distances[destination]}\n' \
           f'{path}'


if __name__ == '__main__':
    print(main())
