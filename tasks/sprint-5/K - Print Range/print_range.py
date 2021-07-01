from node import Node


def print_range(root: Node, left: int, right: int) -> None:
    if root is None:
        return

    if left <= root.value:
        print_range(root.left, left, right)

    if left <= root.value <= right:
        print(root.value)

    if right >= root.value:
        print_range(root.right, left, right)
