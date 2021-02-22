from node import Node
from solution import solution


def main(head: Node):
    solution(head)


if __name__ == '__main__':
    main(Node('Head', next_item=Node('Next', next_item=Node('Finish'))))
