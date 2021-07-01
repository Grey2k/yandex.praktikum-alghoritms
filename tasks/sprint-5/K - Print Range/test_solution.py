from node import Node
from print_interval import print_interval


def print_tree(node: Node, _prefix="", _last=True):
    if node is None:
        return

    print(_prefix, "- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "

    if node.left is not None:
        print_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node.right is not None:
        print_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


def main():
    root = Node(5,
                Node(1, right=Node(2)),
                Node(10,
                     Node(10, Node(9, Node(8, right=Node(8))))
                     )
                )
    print_tree(root)
    print('====')
    print_interval(root, 2, 8)
    print('====')


if __name__ == '__main__':
    main()
