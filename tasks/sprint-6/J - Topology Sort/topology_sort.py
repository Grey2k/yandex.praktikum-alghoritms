# from typing import Dict, List
# from draw import nx, draw

COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type Dict[int, List[int]]
    colors = [COLOR_WHITE for n in range(n + 1)]
    order = [(0, 0) for m in range(m)]

    # graph = nx.DiGraph()
    # graph.add_nodes_from(range(1, n + 1))

    for i in range(m):
        u, v = map(int, input().strip().split())
        # graph.add_edge(u, v)
        adjacency_list.get(u).append(v)
        order[i] = (u, v)

    # print(adjacency_list)
    # print(colors)

    # draw(graph)

    dag = []
    for u, _ in order:
        if colors[u] == COLOR_WHITE:
            topology_sort(u, adjacency_list, colors, dag)

    for i in range(1, n + 1)[::-1]:
        if colors[i] == COLOR_WHITE:
            topology_sort(i, adjacency_list, colors, dag)

    print(' '.join(map(str, reversed(dag))))


def topology_sort(v: int, graph: dict, colors: list, dag: list):
    colors[v] = COLOR_GRAY

    for node in graph.get(v):
        if colors[node] == COLOR_WHITE:
            topology_sort(node, graph, colors, dag)

    colors[v] = COLOR_BLACK
    dag.append(v)


if __name__ == '__main__':
    main()
