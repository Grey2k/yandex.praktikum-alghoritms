def solution(node, value):
    i = 0
    if node.value == value:
        return 0

    while node.next_item is not None:
        node = node.next_item
        i += 1

        if node.value == value:
            return i

    return -1
