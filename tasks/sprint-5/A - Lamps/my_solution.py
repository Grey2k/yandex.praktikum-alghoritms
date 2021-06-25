def solution(node) -> int:
    root_value = node.value

    if (node.left is None) and (node.right is None):
        return root_value

    if node.left is not None:
        left_value = solution(node.left)
    else:
        left_value = 0

    if node.right is not None:
        right_value = solution(node.right)
    else:
        right_value = 0

    return max(root_value, left_value, right_value)
