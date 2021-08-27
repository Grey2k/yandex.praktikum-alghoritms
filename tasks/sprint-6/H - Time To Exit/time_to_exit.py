# from typing import Dict, List
# from draw import nx, draw
from collections import deque

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

    distance = {start: 0}
    bfs(start, adjacency_list, colors, distance)
    print(str(max(distance.values())))


def bfs(start: int, graph: dict, colors: dict, distance: dict) -> None:
    planned = deque([start])
    previous = {}
    colors[start] = COLOR_GRAY

    while len(planned) > 0:
        u = planned.pop()
        for v in sorted(graph.get(u)):
            if colors[v] == COLOR_WHITE:
                distance[v] = distance[u] + 1
                previous[v] = u
                colors[v] = COLOR_GRAY
                planned.appendleft(v)

        colors[u] = COLOR_BLACK


if __name__ == '__main__':
    main()
