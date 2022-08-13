from collections import deque


def get_graph():
    graph = {}

    stories = input()
    while stories != 'End':
        args = stories.split('->')
        node = args[0].strip()
        graph[node] = [] if len(args) < 2 else args[1].strip().split()
        stories = input()

    return graph


def dfs(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.appendleft(node)


def main():
    graph = get_graph()
    result = deque()
    visited = set()

    for node in graph:
        dfs(node, graph, visited, result)

    return ' '.join(result)


if __name__ == '__main__':
    print(main())
