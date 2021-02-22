from node import Node


def solution(node: Node, idx: int) -> Node:
    i = idx
    neighbour = None
    head = node

    if i == 0:
        return node.next_item

    while i > 0:
        if i == 1:
            neighbour = node

        node = node.next_item
        i -= 1

    neighbour.next_item = node.next_item
    return head
