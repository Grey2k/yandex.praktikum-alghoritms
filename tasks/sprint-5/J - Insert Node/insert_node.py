from node import Node


def insert(root: Node, key) -> Node:
    if root is None:
        root = Node(value=key)
        return root

    if key < root.value:
        if root.left is not None:
            insert(root.left, key)
        else:
            root.left = Node(value=key)

    elif key >= root.value:
        if root.right is not None:
            insert(root.right, key)
        else:
            root.right = Node(value=key)

    return root
