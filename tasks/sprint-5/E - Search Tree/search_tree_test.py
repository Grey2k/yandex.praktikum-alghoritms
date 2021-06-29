import unittest

from node import Node
from search_tree import solution


def print_tree(node: Node, _prefix="", _last=True):
    print(_prefix, "- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "

    if node.left is not None:
        print_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node.right is not None:
        print_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


class SearchTreeTest(unittest.TestCase):
    def test_edge(self):
        node = Node(0)
        print()
        print_tree(node)
        self.assertEqual(solution(node), True)

    def test_none(self):
        print()
        # noinspection PyTypeChecker
        self.assertEqual(solution(None), True)

    def test_big(self):
        root1 = Node(1,
                     Node(3,
                          Node(8,
                               Node(14), Node(15)
                               ),
                          Node(10,
                               right=Node(3)
                               )
                          ),
                     Node(5,
                          Node(2), Node(6,
                                        Node(0), Node(1)
                                        )
                          ))

        print()
        print_tree(root1)
        self.assertEqual(solution(root1), False)

    def test_one(self):
        root1 = Node(5,
                     Node(3,
                          Node(1), Node(4)
                          ),
                     Node(8)
                     )

        print()
        print_tree(root1)
        self.assertEqual(solution(root1), True)

    def test_two(self):
        root1 = Node(5,
                     Node(3,
                          Node(1), Node(5)
                          ),
                     Node(8)
                     )

        print()
        print_tree(root1)
        self.assertEqual(solution(root1), False)

    def test_three(self):
        root1 = Node(3,
                     Node(1), Node(5)
                     )

        print()
        print_tree(root1)
        self.assertEqual(solution(root1), True)

    def test_four(self):
        root1 = Node(3,
                     Node(3), Node(3)
                     )

        print()
        print_tree(root1)
        self.assertEqual(solution(root1), False)
