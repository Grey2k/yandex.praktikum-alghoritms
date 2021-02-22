import unittest
import io
from unittest.mock import patch

from solution import solution
from node import Node


def print_list(node: Node) -> None:
    while node.next_item is not None:
        print(node.value)
        node = node.next_item

    print(node.value)


class LeastFavoriteTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        print_list(solution(Node('Head', next_item=Node('Next', next_item=Node('Finish'))), 2))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Head',
            'Next',
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        print_list(solution(Node('Head', next_item=Node('Next', next_item=Node('Finish'))), 1))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Head',
            'Finish',
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        print_list(solution(Node('Head', next_item=Node('Next')), 0))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Next'
        ]) + '\n')
