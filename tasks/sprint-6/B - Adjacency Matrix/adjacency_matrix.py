# from draw import nx, draw


def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # graph = nx.DiGraph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v = map(int, input().strip().split())
        # graph.add_edge(u, v)
        adjacency_matrix[u - 1][v - 1] = 1

    # print(adjacency_matrix)

    for line in adjacency_matrix:
        print(' '.join(map(str, line)))

    # draw(graph)


if __name__ == '__main__':
    main()
