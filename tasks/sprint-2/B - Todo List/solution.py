from node import Node


def solution(node: Node) -> None:
    while node.next_item is not None:
        print(node.value)
        node = node.next_item

    print(node.value)
