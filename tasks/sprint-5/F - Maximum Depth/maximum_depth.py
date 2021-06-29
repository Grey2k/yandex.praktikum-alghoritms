from node import Node


def solution(root: Node) -> int:
    return tree_depth(root)


def tree_depth(root: Node) -> int:
    if root is None:
        return 0

    left_depth = tree_depth(root.left)
    right_depth = tree_depth(root.right)

    return left_depth + 1 if left_depth > right_depth else right_depth + 1
