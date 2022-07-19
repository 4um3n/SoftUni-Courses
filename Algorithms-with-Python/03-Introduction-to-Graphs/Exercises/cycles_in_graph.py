def get_graph():
    graph = {}
    pair = input()

    while pair != 'End':
        node, child = pair.split('-')

        if node not in graph:
            graph[node] = []

        graph[node].append(child)
        pair = input()

    return graph


def get_edges(graph):
    edges = {}

    for node, children in graph.items():
        if node not in edges:
            edges[node] = 0

        for child in children:
            if child not in edges:
                edges[child] = 0
            edges[child] += 1

    return edges


def is_acyclical(edges):
    for node, value in edges.items():
        if value == 0:
            return 'Acyclic: Yes'

    return 'Acyclic: No'


if __name__ == '__main__':
    print(is_acyclical(get_edges(get_graph())))


# K-J
# J-N
# N-L
# N-M
# M-I
# End
