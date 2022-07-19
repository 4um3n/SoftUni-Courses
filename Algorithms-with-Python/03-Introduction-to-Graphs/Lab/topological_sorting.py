def get_zero_dependencies_node(dependencies):
    for node, value in dependencies.items():
        if value == 0:
            return node


def topological_sort(nodes, dependencies):
    sorted_nodes = []

    while dependencies:
        node = get_zero_dependencies_node(dependencies)

        if not node:
            return 'Invalid topological sorting'

        sorted_nodes.append(node)
        dependencies.pop(node)

        for child in nodes[node]:
            dependencies[child] -= 1

    return f'Topological sorting: {", ".join(sorted_nodes)}'


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


def main():
    graph = {}

    for _ in range(int(input())):
        node, children = [el.strip() for el in input().split('->')]
        graph[node] = children.split(', ') if children else []

    edges = get_edges(graph)
    return topological_sort(graph, edges)


if __name__ == '__main__':
    print(main())


# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->
