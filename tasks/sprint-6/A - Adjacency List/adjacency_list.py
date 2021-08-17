# from draw import nx, draw


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type: dict[list]

    # graph = nx.DiGraph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v = map(int, input().strip().split())
        # graph.add_edge(u, v)
        adjacency_list.get(u).append(v)

    # print(adjacency_list)

    for item in adjacency_list.values():
        print(f"{len(item)} {' '.join(map(str, sorted(item)))}")

    # draw(graph)


if __name__ == '__main__':
    main()
