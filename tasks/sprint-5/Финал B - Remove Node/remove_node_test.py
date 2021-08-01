import unittest

from typing import Optional
from node import Node
from remove_node import remove


def print_tree(node: Optional[Node], _prefix="", _last=True):
    print(_prefix, "- " if _last else "|- ", node.value if node is not None else None, sep="")
    _prefix += "   " if _last else "|  "

    if node is not None and node.left is not None:
        print_tree(node.left, _prefix, (node.left.left is None) and (node.left.right is None))
    if node is not None and node.right is not None:
        print_tree(node.right, _prefix, (node.right.left is None) and (node.right.right is None))


def tree_equal(first: Optional[Node], second: Optional[Node]):
    if first is None and second is None:
        return True

    if first is None or second is None:
        return False

    return first.value == second.value and \
           tree_equal(first.left, second.left) and \
           tree_equal(first.right, second.right)


class RemoveNodeTest(unittest.TestCase):
    def test_edge(self):
        root = Node(value=7)

        print()
        result = remove(root, 7)
        print_tree(result)
        self.assertEqual(result, None, True)

    def test_one(self):
        root = Node(
            left=Node(value=3),
            value=7
        )

        print()
        result = remove(root, 3)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=7)), True)

    def test_two(self):
        root = Node(
            left=Node(value=42),
            right=Node(value=45),
            value=43
        )

        print()
        result = remove(root, 43)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(value=42,
                                                 right=Node(value=45)
                                                 )), True)

    def test_three(self):
        root = Node(
            left=Node(
                left=Node(value=42),
                right=Node(value=45),
                value=43
            ),
            right=Node(value=90),
            value=70)
        print()
        result = remove(root, 43)
        print_tree(result)
        self.assertEqual(tree_equal(result, Node(
            left=Node(
                right=Node(value=45),
                value=42
            ),
            right=Node(value=90),
            value=70)), True)
