import unittest
import io
from unittest.mock import patch

from solution import solution
from node import DoubleConnectedNode


def print_list(node: DoubleConnectedNode) -> None:
    while node.next is not None:
        print(node.value)
        node = node.next

    print(node.value)


class OtherWayAroundTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        head = DoubleConnectedNode('Head')

        print_list(solution(head))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Head'
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        head = DoubleConnectedNode('Head')
        tail = DoubleConnectedNode('Tail', prev=head)
        head.next = tail

        print_list(solution(head))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Tail',
            'Head'
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        head = DoubleConnectedNode('Head')
        tail = DoubleConnectedNode('Tail')
        middle = DoubleConnectedNode('Next', prev=head, next=tail)
        head.next = middle
        tail.prev = middle

        print_list(solution(head))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Tail',
            'Next',
            'Head'
        ]) + '\n')
