import unittest
import io
from unittest.mock import patch

from solution import solution
from node import Node


class CaringMotherTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        print(solution(Node('Head', next_item=Node('Next', next_item=Node('Finish'))), 'Finish'))
        self.assertEqual(stdout.getvalue(), "\n".join([
            '2'
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        print(solution(Node('Head', next_item=Node('Next', next_item=Node('Finish'))), 'Head'))
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0'
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        print(solution(Node('Head', next_item=Node('Next', next_item=Node('Finish'))), 'None'))
        self.assertEqual(stdout.getvalue(), "\n".join([
            '-1'
        ]) + '\n')
