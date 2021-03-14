import unittest
import io
from unittest.mock import patch

from partial_sort import main


class PartialSortTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '4',
        '0 1 3 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '3 6 7 4 1 5 0 2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '1 0 2 3 4',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    def test_edge(self):
        pass
