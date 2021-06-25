import unittest

from node import Node
from lamps import solution


def pprint_tree(node: Node, _prefix="", _last=True):
    print(_prefix, "- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "

    if node.left is not None:
        pprint_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node.right is not None:
        pprint_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


class LampsTest(unittest.TestCase):
    def test_edge(self):
        node = Node(0)
        print()
        pprint_tree(node)
        self.assertEqual(solution(node), 0)

    def test_one(self):
        node = Node(1,
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
        pprint_tree(node)
        self.assertEqual(solution(node), 15)
