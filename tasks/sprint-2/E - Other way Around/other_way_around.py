from node import DoubleConnectedNode
from solution import solution


def print_list(node: DoubleConnectedNode) -> None:
    while node.next is not None:
        print(node.value)
        node = node.next

    print(node.value)


def main(list_head: DoubleConnectedNode):
    print_list(solution(list_head))


if __name__ == '__main__':
    head = DoubleConnectedNode('Head')
    tail = DoubleConnectedNode('Tail')
    middle = DoubleConnectedNode('Next', prev=head, next=tail)
    head.next = middle
    tail.prev = middle

    main(head)
