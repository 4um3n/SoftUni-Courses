from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.price


def get_graph(nodes_count, edges_count):
    graph = [[] for _ in range(nodes_count)]
    tree = set()

    for _ in range(edges_count):
        edge_data = input().split()
        source, destination, weight = [int(x) for x in edge_data[:3]]

        if len(edge_data) == 4:
            tree.add(source)
            tree.add(destination)

        edge = Edge(source, destination, weight)
        graph[source].append(edge)
        graph[destination].append(edge)

    return graph, tree


def prim(budget, graph, tree):
    edges_pq = PriorityQueue()
    for node in tree:
        for edge in graph[node]:
            edges_pq.put(edge)

    while not edges_pq.empty():
        min_edge = edges_pq.get()
        non_tree_node = None

        if min_edge.source not in tree and min_edge.destination in tree:
            non_tree_node = min_edge.source
        elif min_edge.destination not in tree and min_edge.source in tree:
            non_tree_node = min_edge.destination

        if non_tree_node is None:
            continue

        if budget - min_edge.price < 0:
            break

        tree.add(non_tree_node)
        budget -= min_edge.price

        for e in graph[non_tree_node]:
            edges_pq.put(e)

    return budget


def main():
    budget = int(input())
    nodes_count = int(input())
    edges_count = int(input())
    graph, tree = get_graph(nodes_count, edges_count)
    budget_left = prim(budget, graph, tree)
    return f'Budget used: {budget - budget_left}'


if __name__ == '__main__':
    print(main())
