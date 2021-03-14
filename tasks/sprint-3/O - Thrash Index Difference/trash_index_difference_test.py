import unittest
import io
from unittest.mock import patch

from trash_index_difference import main


class TrashIndexDifferenceTests(unittest.TestCase):

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '2 3 4',
        '2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '1 3 1',
        '1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '3',
        '1 3 5',
        '3',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '4',
        ]) + '\n')

    def test_edge(self):
        pass
