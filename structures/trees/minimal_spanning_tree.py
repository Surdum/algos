from collections import defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(int)
        self.vertices = set()

    def add_edge(self, from_, to_, weight=1):
        self.vertices.add(from_)
        self.vertices.add(to_)
        self.edges[(from_, to_)] = weight

    def __str__(self):
        s = []
        for edge in self.edges:
            s.append(f'{edge[0]}{edge[1]}: {self.edges[edge]}')
        return ', '.join(s)


def mst_kraskal(_graph: Graph):
    def find_root(vert):
        while subsets[vert] != vert:
            vert = subsets[vert]
        return vert

    edge_count = 0
    target_edge_count = len(_graph.vertices) - 1
    subsets = {vert: vert for vert in _graph.vertices}
    edges = sorted(_graph.edges, key=lambda x: _graph.edges[x])
    span_tree = Graph()
    for edge in edges:
        v1, v2 = edge
        if find_root(v1) != find_root(v2):
            subsets[find_root(v1)] = v2
            span_tree.add_edge(v1, v2, _graph.edges[edge])
            edge_count += 1
        if edge_count == target_edge_count:
            break
    return span_tree


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge("a", "b", 3)
    graph.add_edge("a", "e", 1)
    graph.add_edge("b", "e", 4)
    graph.add_edge("b", "c", 5)
    graph.add_edge("e", "c", 6)
    graph.add_edge("c", "d", 2)
    graph.add_edge("e", "d", 7)
    print('Original graph:', graph)
    print()

    min_span_tree = mst_kraskal(graph)
    print('MinSpanin tree:', min_span_tree)








