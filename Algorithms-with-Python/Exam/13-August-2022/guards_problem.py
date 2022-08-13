from collections import deque


def get_graph(nodes, edges):
    graph = [[] for _ in range(nodes + 1)]

    for _ in range(edges):
        source, destination = [int(n) for n in input().split()]
        graph[source].append(destination)

    return graph


def dfs(node, graph, visited):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


def get_path(nodes, visited):
    path = deque()

    for n in range(1, nodes + 1):
        if n not in visited:
            path.append(n)

    return path


def main():
    nodes = int(input())
    edges = int(input())
    graph = get_graph(nodes, edges)
    start_node = int(input())
    visited = set()
    dfs(start_node, graph, visited)
    path = get_path(nodes, visited)
    return ' '.join([str(n) for n in path])


if __name__ == '__main__':
    print(main())
