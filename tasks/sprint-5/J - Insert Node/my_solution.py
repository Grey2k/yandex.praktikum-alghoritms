from node import Node


# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
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


def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
