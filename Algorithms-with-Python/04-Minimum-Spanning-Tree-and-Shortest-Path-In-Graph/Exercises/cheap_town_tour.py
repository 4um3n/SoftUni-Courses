class Street:
    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost


def get_graph(streets_count):
    graph = []

    for _ in range(streets_count):
        source, destination, cost = [int(n) for n in input().split(' - ')]
        graph.append(Street(source, destination, cost))

    return graph


def get_root(node, roots):
    while node != roots[node]:
        node = roots[node]

    return node


def kruskal(towns_count, graph):
    roots = [n for n in range(towns_count)]
    country = []

    for street in sorted(graph, key=lambda s: s.cost):
        source_root = get_root(street.source, roots)
        destination_root = get_root(street.destination, roots)

        if source_root != destination_root:
            country.append(street)
            roots[source_root] = destination_root

    return country


def main():
    towns_count = int(input())
    streets_count = int(input())
    graph = get_graph(streets_count)
    country = kruskal(towns_count, graph)
    cost = sum([s.cost for s in country])
    return f'Total cost: {cost}'


if __name__ == '__main__':
    print(main())
