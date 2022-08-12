from queue import PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def get_graph(nodes, edges):
    graph = {node: [] for node in range(nodes)}

    for _ in range(edges):
        source, destination, damage = [int(n) for n in input().split()]
        edge = Edge(source, destination, damage)
        graph[source].append(edge)
        graph[destination].append(edge)

    return graph


def calc_damage(damage, jumps):
    for _ in range(jumps):
        damage //= 2

    return damage


def prim(node, graph, damage, damage_by_node):
    damage_by_node[node] += damage
    jumps = [0] * len(graph)
    visited = {node}

    pq = PriorityQueue()
    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        min_edge = pq.get()
        tree_node, non_tree_node = None, None

        if min_edge.source in visited and min_edge.destination not in visited:
            tree_node, non_tree_node = min_edge.source, min_edge.destination
        elif min_edge.destination in visited and min_edge.source not in visited:
            tree_node, non_tree_node = min_edge.destination, min_edge.source

        if tree_node is None:
            continue

        visited.add(non_tree_node)

        for edge in graph[non_tree_node]:
            pq.put(edge)

        jumps[non_tree_node] = jumps[tree_node] + 1
        damage_by_node[non_tree_node] += calc_damage(damage, jumps[non_tree_node])


def main():
    nodes = int(input())
    edges = int(input())
    lightnings = int(input())
    graph = get_graph(nodes, edges)
    damage_by_node = [0] * nodes

    for _ in range(lightnings):
        node, damage = [int(n) for n in input().split()]
        prim(node, graph, damage, damage_by_node)

    return max(damage_by_node)


if __name__ == '__main__':
    print(main())
