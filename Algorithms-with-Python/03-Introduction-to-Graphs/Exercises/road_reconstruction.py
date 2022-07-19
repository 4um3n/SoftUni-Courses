def get_data():
    nodes_count = int(input())
    edges_count = int(input())
    graph = [[] for _ in range(nodes_count)]
    edges = set()

    for _ in range(edges_count):
        node, child = [int(n) for n in input().split(' - ')]
        graph[node].append(child)
        graph[child].append(node)
        edges.add((min(node, child), max(node, child)))

    return graph, edges, nodes_count


def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(graph, child, visited)


def get_important_streets(graph, edges, nodes_count):
    message = ['Important streets:']

    for source, destination in edges:
        graph[source].remove(destination)
        graph[destination].remove(source)

        visited = set()
        dfs(graph, source, visited)

        if len(visited) < nodes_count:
            message.append(f'{source} {destination}')

        graph[source].append(destination)
        graph[destination].append(source)

    return '\n'.join(message)


def main():
    graph, edges, nodes_count = get_data()
    return get_important_streets(graph, edges, nodes_count)


if __name__ == '__main__':
    print(main())
