import unittest
import io
from unittest.mock import patch

from merge_algo import merge, merge_sort
from merge_sort import main


class BubbleTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '4 3 9 2 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1 2 3 4 9',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '12 8 9 10 11',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '8 9 10 11 12',
        ]) + '\n')

    def test_edge(self):
        pass
