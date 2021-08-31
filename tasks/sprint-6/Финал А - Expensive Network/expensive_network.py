# from typing import Dict, List
import math
from draw import nx, draw


def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[math.inf for _ in range(n)] for _ in range(n)]

    graph = nx.Graph()
    graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        graph.add_edge(u, v, weight=w)
        if adjacency_matrix[u - 1][v - 1] > w:
            adjacency_matrix[u - 1][v - 1] = w
            adjacency_matrix[v - 1][u - 1] = w

    start = 1

    print(adjacency_matrix)
    draw(graph)

    mst = []
    edges = []

    try:
        find_mst(adjacency_matrix, mst)
        print(str(sum([v[1] for v in mst])))
    except ValueError as e:
        print(e)


def find_mst(adjacency_matrix: list, edges: list, mst: list):
    not_added = {v for v in range(1, len(adjacency_matrix) + 1)}
    added = {}

    start = 1
    add_vertex(start)

    while len(not_added) > 0 and len(edges) > 0:
        e = extract_minimum(edges)
        if e.end in not_added:
            mst.append(e)
            add_vertex(e.end)

    if len(not_added) > 0:
        ValueError('Oops! I did it again')

    return mst


def add_vertex(v: int, graph: list, added: set, not_added: set, edges: list):
    pass


def extract_minimum(edges: list):
    pass


if __name__ == '__main__':
    main()
