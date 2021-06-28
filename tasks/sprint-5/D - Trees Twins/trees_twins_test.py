import unittest

from node import Node
from trees_twins import solution


def print_tree(node: Node, _prefix="", _last=True):
    print(_prefix, "- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "

    if node.left is not None:
        print_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node.right is not None:
        print_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


class SymmetricTreeTest(unittest.TestCase):
    def test_edge(self):
        node = Node(0)
        print()
        print_tree(node)
        self.assertEqual(solution(node, node), True)

    def test_none(self):
        print()
        self.assertEqual(solution(None, None), True)

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

        root2 = Node(1,
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
        print_tree(root2)
        self.assertEqual(solution(root1, root2), True)

    def test_one(self):
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

        root2 = Node(1,
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
                                        Node(11), Node(1)
                                        )
                          ))
        print()
        print_tree(root1)
        print_tree(root2)
        self.assertEqual(solution(root1, root2), False)
