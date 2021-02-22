from node import Node
from solution import solution


def print_list(node: Node) -> None:
    while node.next_item is not None:
        print(node.value)
        node = node.next_item

    print(node.value)


def main(head: Node):
    print_list(solution(head, 2))


if __name__ == '__main__':
    main(Node('Head', next_item=Node('Next', next_item=Node('Finish'))))
