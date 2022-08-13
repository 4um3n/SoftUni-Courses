from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

    def __gt__(self, other):
        return self.distance > other.price

    def __str__(self):
        return f'{self.source} - {self.destination}'


def get_graph(edges_count):
    graph = {}

    for _ in range(edges_count):
        source, destination, distance = [int(x) for x in input().split(', ')]
        
        if source not in graph:
            graph[source] = []
            
        if destination not in graph:
            graph[destination] = []
            
        edge = Edge(source, destination, distance)
        graph[source].append(edge)
        graph[destination].append(edge)

    return graph


def prim(node, forest, edges_forest, graph):
    forest.add(node)

    edges_pq = PriorityQueue()
    for edge in graph[node]:
        edges_pq.put(edge)

    while not edges_pq.empty():
        min_edge = edges_pq.get()
        non_tree_node = None
        
        if min_edge.source not in forest and min_edge.destination in forest:
            non_tree_node = min_edge.source
        elif min_edge.destination not in forest and min_edge.source in forest:
            non_tree_node = min_edge.destination
        
        if non_tree_node is None:
            continue

        forest.add(non_tree_node)
        edges_forest.append(min_edge)

        for e in graph[non_tree_node]:
            edges_pq.put(e)


def main():
    edges_count = int(input())
    graph = get_graph(edges_count)
    forest = set()
    forest_edges = []

    for node in graph.keys():
        if node in forest:
            continue

        prim(node, forest, forest_edges, graph)

    return '\n'.join([str(e) for e in forest_edges])


if __name__ == '__main__':
    print(main())
