import unittest

from node import Node
from symmetric_tree import solution


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
        self.assertEqual(solution(node), True)

    def test_none(self):
        print()
        self.assertEqual(solution(None), True)

    def test_big(self):
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
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_one(self):
        node = Node(1, Node(2), Node(0))
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_two(self):
        node = Node(1,
                    Node(2),
                    Node(0,
                         Node(3), Node(6)
                         )
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_three(self):
        node = Node(0,
                    Node(2), Node(7,
                                  Node(4,
                                       Node(12)
                                       ), Node(8)
                                  )
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_four(self):
        node = Node(0,
                    Node(2,
                         Node(7)
                         )
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_five(self):
        node = Node(1,
                    Node(1),
                    Node(3, right=Node(8,
                                       Node(4,
                                            right=Node(7, Node(5, right=Node(6)))
                                            ),
                                       Node(10,
                                            Node(9),
                                            Node(11)
                                            )
                                       )
                         )
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_six(self):
        node = Node(12,
                    Node(8,
                         Node(6,
                              right=Node(2)
                              ), Node(10)
                         ),
                    Node(15, Node(14))
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_seven(self):
        node = Node(1,
                    Node(2, Node(4), Node(3)),
                    Node(2, Node(3), Node(4))
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), True)

    def test_eight(self):
        node = Node(1,
                    Node(2, right=Node(3)),
                    Node(2, right=Node(3))
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_nine(self):
        node = Node(1,
                    Node(2, right=Node(3)),
                    Node(2)
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)

    def test_ten(self):
        node = Node(1,
                    Node(2),
                    Node(2, right=Node(3))
                    )
        print()
        print_tree(node)
        self.assertEqual(solution(node), False)
