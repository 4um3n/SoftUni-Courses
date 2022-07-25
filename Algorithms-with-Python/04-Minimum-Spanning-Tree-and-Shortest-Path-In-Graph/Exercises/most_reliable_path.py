from collections import deque
from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def get_graph(edges_count):
    graph = {}

    for _ in range(edges_count):
        source, destination, weight = [int(n) for n in input().split()]

        if source not in graph:
            graph[source] = []

        if destination not in graph:
            graph[destination] = []

        edge = Edge(source, destination, weight)
        graph[source].append(edge)
        graph[destination].append(edge)

    return graph


def dijkstra(nodes_count, source, destination, graph):
    parents = [None] * nodes_count
    distances = [float('-inf')] * nodes_count
    distances[source] = 100

    distances_pq = PriorityQueue()
    distances_pq.put((-100, source))

    while not distances_pq.empty():
        min_distance, node = distances_pq.get()
        max_distance = -min_distance

        if node == destination:
            break

        for edge in graph[node]:
            child = edge.source if edge.destination == node else edge.destination
            current_distance = (max_distance * edge.weight) / 100

            if current_distance > distances[child]:
                distances[child] = current_distance
                parents[child] = node
                distances_pq.put((-current_distance, child))

    return parents, distances


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
    parents, distances = dijkstra(nodes_count, source, destination, graph)
    path = get_path(destination, parents)

    return '\n'.join([
        f'Most reliable path reliability: {distances[destination]:.2f}%',
        ' -> '.join([str(n) for n in path])
    ])


if __name__ == '__main__':
    print(main())
