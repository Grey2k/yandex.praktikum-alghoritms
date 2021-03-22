import unittest
import io
from unittest.mock import patch

from sum_of_fours import main


class CommonSubarrayTest(unittest.TestCase):
    @patch('sys.stdin', io.StringIO("\n".join([
        '8',
        '10',
        '2 3 2 4 1 10 3 0',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_one(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '0 3 3 4',
            '1 2 3 4',
            '2 2 3 3',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '6',
        '0',
        '1 0 -1 0 2 -2',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_two(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '3',
            '-2 -1 1 2',
            '-2 0 0 2',
            '-1 0 0 1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '5',
        '4',
        '1 1 1 1 1',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_three(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '1',
            '1 1 1 1',
        ]) + '\n')

    @patch('sys.stdin', io.StringIO("\n".join([
        '0',
        '0',
        '',
    ])))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_four(self, stdout):
        main()
        self.assertEqual(stdout.getvalue(), "\n".join([
            '0',
        ]) + '\n')
