"""
-- ПРИНЦИП РАБОТЫ --
В данной задаче мы ищем вершину заданного значения, а дальше реализуем алгоритм
в зависимости от ситуации и структуры дерева. Так же учитываем граничную ситуацию когда вершина
сама является корнем всего дерева. Так как значения в дереве уникальны - то алгоритм будет работать
корректно при единичном проходе дерева поиска.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами и соответствует алгоритму

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Дерево является деревом поиска, поэтому мы проходим по нему за O(H) - где H высота дерева
Поиск максимального элемента в поддереве тоже будет соответствовать его высоте.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Мы оперируем только ссылками на структуры дерева - и вся память тратится на хранение дерева
Исходя из этого сложность - O(N) где N - кол-во вершин дерева

-- ID успешной посылки --
52259727
"""
from typing import Optional, Tuple

from node import Node


def remove(root: Optional[Node], key: int) -> Optional[Node]:
    if root is None:
        return root

    node_to_remove, parent_of_node_to_remove = find_node(root, None, key)

    # If noting to remove returns original root
    if node_to_remove is None:
        return root

    # Removing found node
    return remove_node(root, parent_of_node_to_remove, node_to_remove)


def remove_node(root: Node, node_parent: Optional[Node], node: Node) -> Optional[Node]:
    left = node.left
    right = node.right

    # 0 Case - Node is root without children
    if node is root and left is None and right is None:
        root = None
        return root

    # 1 Case - Node is root and has children
    if node is root:
        if left is None:
            root = right
        else:
            max_node = find_max_and_remove(left)
            root = max_node

            # if maximum is not left part itself
            if max_node is not left:
                max_node.left = left

            max_node.right = right

        return root

    # 2 Case - Node has no children
    if left is None and right is None:
        if node_parent.left is node:
            node_parent.left = None
        else:
            node_parent.right = None

        return root

    # 3 Case - Node has children
    if left is None:
        if node_parent.left is node:
            node_parent.left = right
        else:
            node_parent.right = right
    else:
        max_node = find_max_and_remove(left)
        if node_parent.left is node:
            node_parent.left = max_node
        else:
            node_parent.right = max_node

        # if maximum is not left part itself
        if max_node is not left:
            max_node.left = left

        max_node.right = right

    return root


def find_max_and_remove(node: Node):
    parent = node
    if parent.right is None:
        return parent

    while True:
        if parent.right.right is None:
            found = parent.right
            parent.right = None
            return found

        parent = parent.right


def find_node(root: Optional[Node], parent: Optional[Node], key: int) -> Tuple[Optional[Node], Optional[Node]]:
    if root is None:
        return None, None

    if root.value == key:
        return root, parent

    if root.value < key:
        return find_node(root.right, root, key)

    if root.value > key:
        return find_node(root.left, root, key)
