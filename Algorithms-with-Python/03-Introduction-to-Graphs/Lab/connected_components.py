def dfs(graph, node, visited: set, result: list):
    if node in visited:
        return

    visited.add(node)

    for child in graph[node]:
        dfs(graph, child, visited, result)

    result.append(node)
    return result


def result_to_text(el):
    return f'Connected component: {" ".join([str(n) for n in el])}'


def main():
    result = []
    visited = set()
    graph = [[int(n) for n in input().split()] for _ in range(int(input()))]

    for node in range(len(graph)):
        if node not in visited:
            result.append(dfs(graph, node, visited, []))

    return '\n'.join(map(result_to_text, result))


if __name__ == '__main__':
    print(main())
