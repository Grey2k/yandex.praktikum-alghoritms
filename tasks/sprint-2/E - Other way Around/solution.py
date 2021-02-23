from node import DoubleConnectedNode


def solution(node: DoubleConnectedNode) -> DoubleConnectedNode:
    while node.next is not None:
        current = node
        node = node.next

        current.next = current.prev
        current.prev = node

    node.next = node.prev
    node.prev = None

    return node
