from node import Node
from solution import solution


def main(head: Node):
    print(solution(head, 'Next'))


if __name__ == '__main__':
    main(Node('Head', next_item=Node('Next', next_item=Node('Finish'))))
