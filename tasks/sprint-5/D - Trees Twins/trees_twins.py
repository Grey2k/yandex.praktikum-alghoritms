from node import Node


def solution(roo1: Node, root2: Node) -> bool:
    return is_equal(roo1, root2)


def is_equal(root_left, root_right) -> bool:
    if root_left is None and root_right is None:
        return True

    if (type(root_left) != type(root_right)) or (root_left.value != root_right.value):
        return False

    return is_equal(root_left.left, root_right.left) and is_equal(root_left.right, root_right.right)
