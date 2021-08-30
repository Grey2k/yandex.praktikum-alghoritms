# from typing import Dict, List
import math
from draw import nx, draw

COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'

DISTANCE_INF = -1


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type Dict[int, List[int]]
    colors = [COLOR_WHITE for n in range(n + 1)]
    distance = [math.inf for n in range(n + 1)]
    parent = [None for n in range(n + 1)]
    visited = [False for n in range(n + 1)]
    distance_matrix = [[DISTANCE_INF for _ in range(n)] for _ in range(n)]

    graph = nx.Graph()
    graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        graph.add_edge(u, v, weight=w)
        adjacency_list.get(u).append((v, w))
        adjacency_list.get(v).append((u, w))

    start = 1

    print(start)
    print(adjacency_list)
    print(colors)

    draw(graph)

    for i, visit in enumerate(visited):
        if i == 0:
            continue

        if not visit:
            dejkstra(i, adjacency_list, distance, visited, parent, distance_matrix)

    # for i in range(1, n + 1):
    #     print(f"{entry[i]} {leave[i]}")

    for line in distance_matrix:
        print(' '.join(map(str, line)))


def dejkstra(start: int, graph: dict, distance: list, visited: list, parent: list, matrix: list) -> None:
    distance[start] = 0
    matrix[start - 1][start - 1] = 0

    while True:
        u = get_min_dist_not_visited_vertex(graph, visited, distance)

        if u is None:
            return

        visited[u] = True
        matrix[u - 1][u - 1] = 0
        for item in graph.get(u):
            relax(u, item[0], graph, distance, parent, matrix)


def get_min_dist_not_visited_vertex(graph: dict, visited: list, distance: list):
    current_minimum = math.inf
    current_minimum_vertex = None

    for v, _ in graph.items():
        if not visited[v] and distance[v] < current_minimum:
            current_minimum = distance[v]
            current_minimum_vertex = v

    return current_minimum_vertex


def relax(u: int, v: int, graph: dict, distance: list, parent: list, matrix: list):
    weight_u_v = [item for item in graph[u] if item[0] == v][0][1] + distance[u]

    if distance[v] > weight_u_v:
        distance[v] = weight_u_v
        parent[v] = u

    matrix[u - 1][v - 1] = weight_u_v
    matrix[v - 1][u - 1] = weight_u_v


if __name__ == '__main__':
    main()
