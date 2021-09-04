from heapq import heappush, heappop


# from draw import nx, draw


def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # graph = nx.Graph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v, w = map(int, input().strip().split())

        # remove loops
        if u == v:
            continue

        # graph.add_edge(u, v, weight=w)

        # remove parallel edges
        if adjacency_matrix[u - 1][v - 1] < w:
            adjacency_matrix[u - 1][v - 1] = w
            adjacency_matrix[v - 1][u - 1] = w

    # print(adjacency_matrix)
    # draw(graph)

    mst = []
    edges = []

    try:
        if n > 1 and m == 0:
            raise ValueError('Oops! I did it again')

        find_mst(adjacency_matrix, edges, mst)
        print(str(sum([-v[0] for v in mst])))
    except ValueError as e:
        print(e)


def find_mst(graph: list, edges: list, mst: list):
    not_added = {v for v in range(1, len(graph) + 1)}
    added = set()

    start = 1
    add_vertex(start, graph, added, not_added, edges)

    while len(not_added) > 0 and len(edges) > 0:
        e = heappop(edges)

        if e[2] in not_added:
            mst.append(e)
            add_vertex(e[2], graph, added, not_added, edges)

    if len(not_added) > 0:
        raise ValueError('Oops! I did it again')

    return mst


def add_vertex(v: int, graph: list, added: set, not_added: set, edges: list):
    added.add(v)
    not_added.remove(v)

    # edge represents as tuple (v, u, w)
    for edge in [(-u[1], v, u[0] + 1) for u in enumerate(graph[v - 1]) if u[1] > 0 and (u[0] + 1) in not_added]:
        heappush(edges, edge)


if __name__ == '__main__':
    main()
