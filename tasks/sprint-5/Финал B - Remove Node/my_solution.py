# from node import Node

def remove(root, key):
    if root is None:
        return root

    node_to_remove, parent_of_node_to_remove = find_node(root, None, key)

    # If noting to remove returns original root
    if node_to_remove is None:
        return root

    # Removing found node

    return remove_node(root, parent_of_node_to_remove, node_to_remove)


def remove_node(root, node_parent, node):
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
            return root
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

    # 2 Case - Node has children
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


def find_max_and_remove(node):
    parent = node
    if parent.right is None:
        return parent

    while True:
        if parent.right.right is None:
            found = parent.right
            parent.right = None
            return found

        parent = parent.right


def find_node(root, parent, key):
    if root is None:
        return None, None

    if root.value == key:
        return root, parent

    if root.value < key:
        return find_node(root.right, root, key)

    if root.value > key:
        return find_node(root.left, root, key)


# noinspection Assert
def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)

    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8
