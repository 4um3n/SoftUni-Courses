def get_graph():
    graph = {}

    for _ in range(int(input())):
        node, children = [el.strip() for el in input().split('->')]
        graph[node] = children.split() if children else []

    return graph


def get_edges(graph):
    edges = []

    for node, children in graph.items():
        for child in children:
            edges.append((node, child))

    return edges


def dfs(graph, node, destination, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(graph, child, destination, visited)


def get_edges_to_remove(graph, edges):
    edges_to_remove = []

    for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
        if destination not in graph[source] or source not in graph[destination]:
            continue

        graph[source].remove(destination)
        graph[destination].remove(source)

        visited = set()
        dfs(graph, source, destination, visited)

        if destination in visited:
            edges_to_remove.append(f'{source} - {destination}')
        else:
            graph[source].append(destination)
            graph[destination].append(source)

    return edges_to_remove


def main():
    graph = get_graph()
    edges = get_edges(graph)
    edges_to_remove = get_edges_to_remove(graph, edges)
    return f'Edges to remove: {len(edges_to_remove)}\n' + '\n'.join(edges_to_remove)


if __name__ == '__main__':
    print(main())
