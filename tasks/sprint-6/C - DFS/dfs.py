# from typing import Dict, List
# from draw import nx, draw

COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type Dict[int, List[int]]
    colors = {(n + 1): COLOR_WHITE for n in range(n)}

    # graph = nx.Graph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v = map(int, input().strip().split())
        # graph.add_edge(u, v)
        adjacency_list.get(u).append(v)
        adjacency_list.get(v).append(u)

    start = int(input().strip())

    # print(start)
    # print(adjacency_list)
    # print(colors)

    # draw(graph)

    path = []
    dfs_stack(start, adjacency_list, colors, path)
    print(' '.join(map(str, path)))


def dfs_stack(start: int, graph: dict, colors: dict, path: list) -> None:
    stack = [start]

    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == COLOR_WHITE:
            colors[v] = COLOR_GRAY
            stack.append(v)
            path.append(v)

            for node in reversed(sorted(graph.get(v))):
                if colors[node] == COLOR_WHITE:
                    stack.append(node)
        elif colors[v] == COLOR_GRAY:
            colors[v] = COLOR_BLACK


def dfs_recursive(v: int, graph: dict, colors: dict, path: list) -> None:
    colors[v] = COLOR_GRAY
    path.append(v)
    for node in sorted(graph.get(v)):
        if colors[node] == COLOR_WHITE:
            dfs_recursive(node, graph, colors, path)

    colors[v] = COLOR_BLACK


if __name__ == '__main__':
    main()
