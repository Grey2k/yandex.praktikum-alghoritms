def solution(node) -> bool:
    balanced = True

    if node is None:
        return balanced

    if (node.left is None) and (node.right is None):
        return balanced

    left_len = 0
    if node.left is not None:
        left_len = tree_len(node.left)

    right_len = 0
    if node.right is not None:
        right_len = tree_len(node.right)

    diff = left_len - right_len

    if abs(diff) <= 1 and solution(node.right) is True and solution(node.left) is True:
        return True

    return False


def tree_len(node):
    if node.left is None and node.right is None:
        return 1

    left_len = 0
    if node.left is not None:
        left_len = tree_len(node.left)

    right_len = 0
    if node.right is not None:
        right_len = tree_len(node.right)

    return 1 + max(left_len, right_len)
