import unittest

from node import Node
from insert_node import insert


def print_tree(node: Node, _prefix="", _last=True):
    print(_prefix, "- " if _last else "|- ", node.value, sep="")
    _prefix += "   " if _last else "|  "

    if node.left is not None:
        print_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node.right is not None:
        print_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


def tree_equal(first: Node, second: Node):
    if first is None and second is None:
        return True

    if first is None or second is None:
        return False

    return first.value == second.value and \
           tree_equal(first.left, second.left) and \
           tree_equal(first.right, second.right)


class InsertNodeTest(unittest.TestCase):
    def test_edge(self):
        root = Node(value=7,
                    right=Node(value=7)
                    )

        print()
        result = insert(root, 7)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=7,
                                                 right=Node(
                                                     value=7,
                                                     right=Node(value=7)
                                                 )
                                                 )), True)

    def test_none(self):
        print()
        # noinspection PyTypeChecker
        result = insert(None, 5)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=5)), True)

    def test_one(self):
        root = Node(value=7,
                    right=Node(
                        value=8,
                        left=Node(value=7)
                    )
                    )

        print()
        result = insert(root, 6)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=7,
                                                 left=Node(value=6),
                                                 right=Node(
                                                     value=8,
                                                     left=Node(value=7)
                                                 )
                                                 )), True)

    def test_two(self):
        root = Node(value=7,
                    right=Node(value=8,
                               left=Node(value=7)
                               )
                    )

        print()
        result = insert(root, 7)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=7,
                                                 right=Node(value=8,
                                                            left=Node(value=7,
                                                                      right=Node(value=7)
                                                                      )
                                                            )
                                                 )
                                    ), True)
