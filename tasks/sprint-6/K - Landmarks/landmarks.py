# from typing import Dict, List
import math

# from draw import nx, draw

DISTANCE_INF = -1


def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[math.inf for _ in range(n)] for _ in range(n)]
    distance_matrix = [[DISTANCE_INF for _ in range(n)] for _ in range(n)]

    # graph = nx.Graph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        # graph.add_edge(u, v, weight=w)
        if adjacency_matrix[u - 1][v - 1] > w:
            adjacency_matrix[u - 1][v - 1] = w
            adjacency_matrix[v - 1][u - 1] = w

    # print(adjacency_matrix)
    # print(colors)
    #
    # draw(graph)

    for node in range(1, n + 1):
        dejkstra(node, adjacency_matrix, distance_matrix)

    for line in distance_matrix:
        print(' '.join(map(str, line)))


def dejkstra(start: int, graph: list, distances: list) -> None:
    distance = [math.inf for _ in range(len(graph) + 1)]
    parent = [None for _ in range(len(graph) + 1)]
    visited = [False for _ in range(len(graph) + 1)]

    distance[start] = 0

    while True:
        u = get_min_dist_not_visited_vertex(graph, visited, distance)

        if u is None:
            return

        visited[u] = True
        distances[u - 1][u - 1] = 0
        for v in [v[0] + 1 for v in enumerate(graph[u - 1]) if v[1] < math.inf]:
            relax(start, u, v, graph, distance, parent, distances)


def get_min_dist_not_visited_vertex(graph: list, visited: list, distance: list):
    current_minimum = math.inf
    current_minimum_vertex = None

    for v in range(1, len(graph) + 1):
        if not visited[v] and distance[v] < current_minimum:
            current_minimum = distance[v]
            current_minimum_vertex = v

    return current_minimum_vertex


def relax(start: int, u: int, v: int, graph: list, distance: list, parent: list, distances: list):
    if parent[u] == v:
        return

    distance_u_v = distance[u] + graph[u - 1][v - 1]

    if distance[v] > distance_u_v:
        distance[v] = distance_u_v
        parent[v] = u

        distances[start - 1][v - 1] = distance[v]
        distances[v - 1][start - 1] = distance[v]


if __name__ == '__main__':
    main()
