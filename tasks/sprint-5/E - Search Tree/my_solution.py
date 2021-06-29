def solution(root) -> bool:
    return is_search_tree(root)


def is_search_tree(root) -> bool:
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if is_tree_less(root.left, root.value) \
            and is_tree_greater(root.right, root.value) \
            and is_search_tree(root.left) \
            and is_search_tree(root.right):
        return True

    return False


def is_tree_less(root, max_value) -> bool:
    if root is None:
        return True

    if root.value >= max_value:
        return False

    return is_tree_less(root.left, max_value) and is_tree_less(root.right, max_value)


def is_tree_greater(root, min_value) -> bool:
    if root is None:
        return True

    if root.value <= min_value:
        return False

    return is_tree_greater(root.left, min_value) and is_tree_greater(root.right, min_value)
