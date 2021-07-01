import unittest
import io
from unittest.mock import patch

from node import Node
from print_range import print_range


class PrintRangeTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edge(self, stdout):
        print_range(Node(0), 0, 0)
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_none(self, stdout):
        print_range(None, 0, 0)
        self.assertEqual(stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_one(self, stdout):
        root = Node(5,
                    Node(1, right=Node(2)),
                    Node(10,
                         Node(10, Node(9, Node(8, right=Node(8))))
                         )
                    )

        print_range(root, 2, 8)
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2',
            '5',
            '8',
            '8'
        ]) + '\n')
