class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

    def __str__(self):
        return f'{self.source} - {self.destination}'


def get_graph(edges):
    graph = []
    max_node = float('-inf')

    for _ in range(edges):
        source, destination, distance = [int(x) for x in input().split(', ')]
        graph.append(Edge(source, destination, distance))
        max_node = max(source, destination, max_node)

    return graph, max_node


def get_root(node, roots):
    while node != roots[node]:
        node = roots[node]

    return node


def kruskal(max_node, graph):
    roots = [n for n in range(max_node + 1)]
    forest = []

    for edge in sorted(graph, key=lambda e: e.price):
        source_root = get_root(edge.source, roots)
        destination_root = get_root(edge.destination, roots)

        if source_root != destination_root:
            forest.append(edge)
            roots[destination_root] = source_root

    return forest


def main():
    edges = int(input())
    graph, max_node = get_graph(edges)
    forest = kruskal(max_node, graph)
    return '\n'.join([str(e) for e in forest])


if __name__ == '__main__':
    print(main())
