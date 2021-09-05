"""
-- ПРИНЦИП РАБОТЫ --
В данной задаче мы реализуем и слегка модифицируем алгоритм Прима для поиска минимального оставного дерева.
Вместо минимума среди множества ребер остова мы ищем максимум в итоге получаем максимально возможный вес остова

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами и соответствует алгоритму

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как для поиска мы используем приоритетную очередь, то сложность в основном будет зависеть от вида графа,
в плотном графе E будет стремиться к V^2,
получается что сложность будет O(E*LogV) - где V - кол во вершин, E - кол-во ребер,
для плотных графов O(V^2) , так как V^2 >> E*LogV

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы храним пары вершин и ребра (w,v,u) соответственно O(V + E), где V - кол во вершин, E - кол-во ребер

-- ID успешной посылки --
52656582
"""
from heapq import heappush, heappop
from typing import Dict


def main():
    n, m = map(int, input().strip().split())

    edges_list = {(n + 1): {} for n in range(n)}  # type: Dict[int, Dict[int]]

    for _ in range(m):
        v, u, w = map(int, input().strip().split())

        # remove loops
        if v == u:
            continue

        # remove parallel edges
        if edges_list.get(u).get(v) is None or edges_list[u].get(v) < w:
            edges_list[v][u] = w
            edges_list[u][v] = w

    mst = []
    edges = []

    try:
        if n > 1 and m == 0:
            raise ValueError('Oops! I did it again')

        find_mst(edges_list, edges, mst)
        print(str(sum([-v[0] for v in mst])))
    except ValueError as e:
        print(e)


def find_mst(graph: dict, edges: list, mst: list):
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


def add_vertex(v: int, graph: dict, added: set, not_added: set, edges: list):
    added.add(v)
    not_added.remove(v)

    # edge represents as tuple (w, v, u) , heapq implements min-heap sort, due to it - weight is negative
    for edge in [(-item[1], v, item[0]) for item in graph.get(v).items() if item[0] in not_added]:
        heappush(edges, edge)


if __name__ == '__main__':
    main()
