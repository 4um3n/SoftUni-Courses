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


def get_dependencies(nodes):
    dependencies = {}

    for node, children in nodes.items():
        if node not in dependencies:
            dependencies[node] = 0

        for child in children:
            if child not in dependencies:
                dependencies[child] = 0
            dependencies[child] += 1

    return dependencies


def main():
    nodes = {}

    for _ in range(int(input())):
        node, children = [el.strip() for el in input().split('->')]
        nodes[node] = children.split(', ') if children else []

    dependencies = get_dependencies(nodes)
    return topological_sort(nodes, dependencies)


if __name__ == '__main__':
    print(main())


# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->
