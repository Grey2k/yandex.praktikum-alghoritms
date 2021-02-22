import unittest
import io
from unittest.mock import patch

from todo_list import main
from node import Node


class TodoListTest(unittest.TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main(Node('Head', next_item=Node('Next', next_item=Node('Finish'))))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Head',
            'Next',
            'Finish',
        ]) + '\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main(Node('Head'))
        self.assertEqual(stdout.getvalue(), "\n".join([
            'Head'
        ]) + '\n')
