"""
-- ПРИНЦИП РАБОТЫ --
Условие задачи было не совсем стандартным, поэтому поломав
голову пошел за помощью и коллеги дали подсказку по тому что можно представить типы дорог в виде направления движения
(думал сперва про перебор пар или расчет двух остовов).
В итоге задача свялась к построению направленного графа и поиска в нем цикла.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами и соответствует алгоритму

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность DFS алгоритма O(V + E) где V - кол во вершин, E - кол-во ребер

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Не учитывая память под сам граф -мы храним вершины на стеке и массив цветов в кол-ве V - поэтому сложность O(V)

-- ID успешной посылки --
52657059
"""
COLOR_WHITE = 'white'
COLOR_GRAY = 'gray'
COLOR_BLACK = 'black'

TYPE_FORWARD = 'B'
# noinspection PyUnusedName
TYPE_BACKWARD = 'R'


def main():
    n = int(input().strip())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type Dict[int, List[int]]
    colors = [COLOR_WHITE for n in range(n + 1)]

    for v in range(1, n):
        for u, t in [(v + i + 1, t) for i, t in enumerate(input().strip())]:

            if t == TYPE_FORWARD:
                adjacency_list.get(v).append(u)
            else:
                adjacency_list.get(u).append(v)

    try:
        for v in range(1, n):
            if colors[v] == COLOR_WHITE:
                dfs_stack(v, adjacency_list, colors)

        print('YES')
    except AssertionError:
        print('NO')


def dfs_stack(start: int, graph: dict, colors: list) -> None:
    stack = [start]
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == COLOR_WHITE:
            colors[v] = COLOR_GRAY
            stack.append(v)

            for node in graph.get(v):
                if colors[node] == COLOR_WHITE:
                    stack.append(node)
                if colors[node] == COLOR_GRAY:
                    raise AssertionError('Cycle Found')
        elif colors[v] == COLOR_GRAY:
            colors[v] = COLOR_BLACK


if __name__ == '__main__':
    main()
