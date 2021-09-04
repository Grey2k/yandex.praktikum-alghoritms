"""
-- ПРИНЦИП РАБОТЫ --
В данной задаче мы реализуем и слегка модифицируем алгоритм Прима для поиска минимального оставного дерева.
Вместо минимума среди множества ребер остова мы ищем максимум в итоге получаем максимально возможный вес остова

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами и соответствует алгоритму

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как для поиска мы используем приоритетную очередь, то сложность в основном будет зависеть от вида графа,
в плотном графе E будет стремиться к V^2,
получается что сложность будет O(V*LogV + E) - где V - кол во вершин, E - кол-во ребер,
для плотных графов O(V^2) , так как V^2 >> V*LogV

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы храним пары вершин и ребра (u,v,w) соответственно O(V + E), где V - кол во вершин, E - кол-во ребер

-- ID успешной посылки --
52621655
"""
from heapq import heappush, heappop


def main():
    n, m = map(int, input().strip().split())

    adjacency_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().strip().split())

        # remove loops
        if u == v:
            continue

        # remove parallel edges
        if adjacency_matrix[u - 1][v - 1] < w:
            adjacency_matrix[u - 1][v - 1] = w
            adjacency_matrix[v - 1][u - 1] = w

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

    # edge represents as tuple (w, v, u) , heapq implements min-heap sort, due to it - weight is negative
    for edge in [(-u[1], v, u[0] + 1) for u in enumerate(graph[v - 1]) if u[1] > 0 and (u[0] + 1) in not_added]:
        heappush(edges, edge)


if __name__ == '__main__':
    main()
