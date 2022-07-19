def get_graph():
    graph = []

    for node in range(int(input())):
        graph.append([])

        for child, el in enumerate(list(input())):
            if el == 'Y':
                graph[node].append(child)

    return graph


def get_node_salary(graph: list, node: int):
    children = graph[node]

    if not children:
        return 1

    salary = 0
    for child in children:
        salary += get_node_salary(graph, child)

    return salary


def get_total_salary(graph):
    salary = 0

    for node in range(len(graph)):
        salary += get_node_salary(graph, node)

    return salary


if __name__ == '__main__':
    print(get_total_salary(get_graph()))
