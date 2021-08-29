# from typing import Dict, List
# from draw import nx, draw

COLOR_DEFAULT = 'white'
COLOR_GRAY = 'gray'


def main():
    n, m = map(int, input().strip().split())

    adjacency_list = {(n + 1): [] for n in range(n)}  # type Dict[int, List[int]]
    component_counter = 1
    colors = [COLOR_DEFAULT for n in range(n + 1)]

    # graph = nx.Graph()
    # graph.add_nodes_from(range(1, n + 1))

    for _ in range(m):
        u, v = map(int, input().strip().split())
        # graph.add_edge(u, v)
        adjacency_list.get(u).append(v)
        adjacency_list.get(v).append(u)

    # print(start)
    # print(adjacency_list)

    # draw(graph)

    for v in range(1, n + 1):
        if colors[v] == COLOR_DEFAULT:
            dfs_components(v, adjacency_list, colors, component_color=component_counter)
            component_counter += 1

    # print(colors)

    components = {}
    for index, v in enumerate(colors):
        if index == 0:
            continue

        if components.get(v) is None:
            components[v] = [index]
        else:
            components[v].append(index)

    print(len(components.keys()))
    for item in components.values():
        print(' '.join(map(str, item)))


def dfs_components(start: int, graph: dict, colors: list, component_color: int) -> None:
    stack = [start]
    while len(stack) > 0:
        v = stack.pop()
        if colors[v] == COLOR_DEFAULT:
            colors[v] = COLOR_GRAY
            stack.append(v)

            for node in sorted(graph.get(v))[::-1]:
                if colors[node] == COLOR_DEFAULT:
                    stack.append(node)
        elif colors[v] == COLOR_GRAY:
            colors[v] = component_color


if __name__ == '__main__':
    main()
